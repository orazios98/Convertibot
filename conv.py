#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, Job, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
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
    update.message.reply_text('Ciao! Mi occupo di convertire numeri tra basi diverse \n Per convertire un numero da una base all\'altra basta semplicemente inviarmi un messaggio contenente 3 cifre separate da uno spazio che in ordine rappresentano: il numero da convertire, la base di partenza,  la base di destinazione. \n Esempio: per convertire 101 dalla base 2 alla base 10 invia "101 2 10"')

def help(bot, update):
    update.message.reply_text('Per convertire un numero da una base all\'altra basta semplicemente inviarmi un messaggio contenente 3 cifre separate da uno spazio che in ordine rappresentano: il numero da convertire, la base di partenza,  la base di destinazione. \n Esempio: per convertire 101 dalla base 2 alla base 10 invia "101 2 10"')



def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def converto(bot, update, num, p, a):
    txt= "Converto " + num + " dalla base " + p + " alla base " + a
    print(txt)
    update.message.reply_text(txt)
    if(p=='2'):
        try:
            newdec=int(num,2)
            newoct=oct(newdec)
            newhex=hex(newdec)
            if(a=='2'): 
                update.message.reply_text("Risultato: ` " + num + " `", parse_mode=ParseMode.MARKDOWN)
            if(a=='8'): 
                update.message.reply_text("Risultato: ` " + str(newoct)[2:]+ " `", parse_mode=ParseMode.MARKDOWN)
            if(a=='10'): 
                update.message.reply_text("Risultato: ` " + str(newdec)+ " `", parse_mode=ParseMode.MARKDOWN)
            if(a=='16'): 
                update.message.reply_text("Risultato: ` " + str(newhex)[2:] + " `", parse_mode=ParseMode.MARKDOWN)
        except ValueError as verr:
            update.message.reply_text('Controlla di aver inserito un numero binario (Cifre in [0,1])')
    if(p=='8'):
        try:
            newdec=int(num,8)
            newbin=bin(newdec)
            newhex=hex(newdec)
            if(a=='2'): 
                update.message.reply_text("Risultato: ` " + str(newbin)[2:] + " `", parse_mode=ParseMode.MARKDOWN)
            if(a=='8'): 
                update.message.reply_text("Risultato: ` " + num + " `", parse_mode=ParseMode.MARKDOWN)
            if(a=='10'): 
                update.message.reply_text("Risultato: ` " + str(newdec) + " `", parse_mode=ParseMode.MARKDOWN)
            if(a=='16'): 
                update.message.reply_text("Risultato: ` " + str(newhex)[2:] + " `", parse_mode=ParseMode.MARKDOWN)
        except ValueError as verr:
            update.message.reply_text('Controlla di aver inserito un numero ottale (Cifre in [1,7])')
    if(p=='10'):
        try:
            newoct=oct(int(num))
            newbin=bin(int(num))
            newhex=hex(int(num))
            if(a=='2'): 
                update.message.reply_text("Risultato: ` " + str(newbin)[2:] + " `", parse_mode=ParseMode.MARKDOWN)
            if(a=='8'): 
                update.message.reply_text("Risultato: ` " + str(newoct)[2:] + " `", parse_mode=ParseMode.MARKDOWN)
            if(a=='10'): 
                update.message.reply_text("Risultato: ` " + num + " `", parse_mode=ParseMode.MARKDOWN)
            if(a=='16'): 
                update.message.reply_text("Risultato: ` " + str(newhex)[2:] + " `", parse_mode=ParseMode.MARKDOWN)
        except ValueError as verr:
            update.message.reply_text('Controlla di aver inserito un numero decimale (Cifre in [1,9])')
    if(p=='16'):
        try:
            newdec=int(num,16)
            newoct=oct(newdec)
            newbin=bin(newdec)
            if(a=='2'): 
                update.message.reply_text("Risultato: ` " + str(newbin)[2:] + " `", parse_mode=ParseMode.MARKDOWN)
            if(a=='8'): 
                update.message.reply_text("Risultato: ` " + str(newoct)[2:] + " `", parse_mode=ParseMode.MARKDOWN)
            if(a=='10'): 
                update.message.reply_text("Risultato: ` " + str(newdec) + " `", parse_mode=ParseMode.MARKDOWN)
            if(a=='16'): 
                update.message.reply_text("Risultato: ` " + num + " `", parse_mode=ParseMode.MARKDOWN)
        except ValueError as verr:
            update.message.reply_text('Controlla di aver inserito un numero esadecimale ({[1,9],[a,f]})')

        


def mess_ricevuto(bot, update):
    splitted = update.message.text.split()
    basi = ['2','8','10','16']
    if(len(splitted)==3):
        pa = splitted[1]
        num = splitted[0]
        de = splitted[2]
        if pa in basi:
            if de in basi:
                converto(bot, update, num,pa,de)
            else:
                update.message.reply_text('Inserisci una base di destinazione valida tra 2,8,10,16')
        else:
            update.message.reply_text('Inserisci una base di partenza valida tra 2,8,10,16')
    else:
        update.message.reply_text('Inserisci correttamente i valori necessari \n [base_di_partenza numero base_destinazione] ')




def main():
    updater = Updater("key")
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    logger.warning("sono partito")


    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, mess_ricevuto))

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
    