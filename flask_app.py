#!/usr/bin/env python

import requests
from flask import Flask, request
import telegram
from message_handlers import bot, setup_dispatcher, webhook
from credentials import TOKEN, APP_URL

app = Flask(__name__)

route_for_webhook = '/' + TOKEN
print(route_for_webhook)


@app.route(route_for_webhook, methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        setup_dispatcher()
        # Retrieve the message in JSON and then transform it to Telegram object
        body = request.get_json(silent=True)
        update = telegram.Update.de_json(body, bot)
        webhook(update)
    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook(APP_URL + '/' + TOKEN)
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/del_webhook', methods=['GET', 'POST'])
def del_webhook():
    s = requests.post('https://api.telegram.org/bot' + TOKEN + '/deleteWebhook')
    if s:
        return "webhook del ok"
    else:
        return "webhook del failed"


@app.route('/')
def index():
    return 'ok'
