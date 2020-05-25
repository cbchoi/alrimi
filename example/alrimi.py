import logging
import telegram
import pymongo
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from instance.credential import *
import example1


user = None
conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.get_database('mongo_db')
collection = db.get_collection('Hisnet')

#진짜 시작
def go(update, context):
    update.message.reply_text('아이디와 비밀번호를 입력해 주세요. ex) /start id pw')
    #collection.insert_one({'id':'id', 'pw' : 'pw', '게시판' : '...', '과제' : '...'})


def start(update, context):
    info = update.message.text
    info_1 = info.split(' ')
    print(update.message.chat_id)
    global user
    user = info_1[1]

    idi = collection.find_one({"id" : user, "pw" : info_1[2]})
    if idi != None:
        print(idi)

    else:
        collection.insert_one({"id" : user, "pw" : info_1[2], "chat_id" : })
        print("hi")

    example1.main(user, info_1[2])

    
    #에러 뜰거 생각하

def echo(update, context):
    """Echo the user message."""
    print(update.message.chat_id)
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def _list(update, context): 
    print(user)
    print("!!!")
    notice = collection.find_one({"id" : "dreamjane921"}, {"_id":False,"게시판":True})
    update.message.reply_text(notice["게시판"])
   

def _HW(update, context):
    home = collection.find_one({"id" : user}, {"_id":False,"과제":True})
    update.message.reply_text(home["과제"])


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    updates = updates = telegram.Bot(TELEGRAM_TOKEN).get_updates()





    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("go", go))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("list", _list))
    dp.add_handler(CommandHandler("hw", _HW))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    #updater.bot.send_message(1166940643, '111')
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()