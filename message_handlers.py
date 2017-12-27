from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from handlers import echo, help, start, doodle, d_answer
from credentials import TOKEN

dispatcher = None
bot = Bot(TOKEN)


def setup_dispatcher():

    global dispatcher
    # Note that update_queue is setted to None and
    # 0 workers are allowed on Google app Engine (If not-->Problems with multithreading)
    dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0)

    # ---Register handlers here---
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("doodle", doodle, pass_args=True))
    dispatcher.add_handler(CommandHandler("d_answer", d_answer, pass_args=True))
    dispatcher.add_handler(MessageHandler([Filters.text], echo))

    return dispatcher


def webhook(update):
    global dispatcher
    # Manually get updates and pass to dispatcher
    dispatcher.process_update(update)
