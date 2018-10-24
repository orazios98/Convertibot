#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, Job, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import requests
import json

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Ciao! Mi occupo di convertire numeri tra basi diverse')


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def bintodec(bot, update, args):
    t=args[0];
    try:
        a=int(t,2)
        update.message.reply_text(a)
    except ValueError as verr:
       update.message.reply_text('Ma cosa hai inserito?')
    except Exception as ex:
        update.message.reply_text('Errore!')




def main():
    updater = Updater("768398023:AAEBxUq0Zves5NTNtW70GfxC_aemwqTGCsU")
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("2to10", bintodec, pass_args=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
    