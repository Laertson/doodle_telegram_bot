from doodle import get_doodles_img


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text="Hi, I'm a bot! While I'm only able to send doodles : )")


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='''/doodle - дудл(ы) за сегодня
    /d_answer - ссылка на дудл(ы) за сегодня''')


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)


def doodle(bot, update, args):
    doodles_array = get_doodles_img()
    if doodles_array is None:
        bot.send_message(chat_id=update.message.chat_id, text="Today no new doodles")
    else:
        if not args:
            for dood in doodles_array:
                if dood[2] != 'gif':
                    bot.send_photo(chat_id=update.message.chat_id, photo=dood[0])
                else:
                    bot.send_document(chat_id=update.message.chat_id, document=dood[0])
        else:
            args.sort()
            if len(args) > len(doodles_array):
                bot.send_message(chat_id=update.message.chat_id, text="To many args")
            elif (int(args[-1])-1) > len(doodles_array):
                bot.send_message(chat_id=update.message.chat_id, text="Some arg is too big")
            else:
                for i in args:
                    i = int(i) - 1
                    if doodles_array[i][2] != 'gif':
                        bot.send_photo(chat_id=update.message.chat_id, photo=doodles_array[i][0])
                    else:
                        bot.send_document(chat_id=update.message.chat_id, document=doodles_array[i][0])


def d_answer(bot, update, args):
    doodles_array = get_doodles_img()
    if doodles_array is None:
        bot.send_message(chat_id=update.message.chat_id, text="Today no new doodles")
    else:
        if not args:
            for dood in doodles_array:
                bot.send_message(chat_id=update.message.chat_id, text=dood[1])

        else:
            args.sort()
            if len(args) > len(doodles_array):
                bot.send_message(chat_id=update.message.chat_id, text="To many args")
            elif (int(args[-1])-1) > len(doodles_array):
                bot.send_message(chat_id=update.message.chat_id, text="Some arg is too big")
            else:
                for i in args:
                    i = int(i) - 1
                    bot.send_message(chat_id=update.message.chat_id, text=doodles_array[i][1])
