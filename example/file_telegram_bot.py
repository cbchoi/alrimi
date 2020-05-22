import logging
import pymongo

#import example1

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from instance.credential import *

conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.get_database('mongo_db')
collection = db.get_collection('customer')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


from pathlib import Path

cur_dir = Path(".")
cur_dir = cur_dir.resolve()

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("아이디를 입력해주세요. ex) /id ")

'''
def id(update, context):
    LOGIN_ID = update.message.Get()
    update.message.reply_text("비밀번호를 입력해주세요. ex) /pw 비밀번호 ")

def pw(update, context):
    LOGIN_PW = update.message.Get()
    update.message.reply_text("성공적입니다.")
'''
'''def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')'''



def ids(update, context,):
<<<<<<< HEAD
    idf = mongo.collection.find({"id" : {"$eq":update.message.text}})

    [print(mongo.results) for mongo.results in mongo.results]
    #else:
     #   mongo.collection.insert_one({'id': update.message.text, 'pw': ' '})
    #print(update.message.chat_id)
=======
    idf = collection.find_one({"id" : {"$eq":update.message.text}})
    if idf != None:
        print(idf["id"])
    else:
        collection.insert_one({'id': update.message.text})
        print("hi")
>>>>>>> 86fa77c87f94a8a61f4cda28ed0dab37afb6dc32

def echo(update, context):
    """Echo the user message."""
    print(update.message.chat_id)
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def _list(update, context):
    update.message.reply_text(mong)

def _parent(update, context):
    global cur_dir
    cur_dir = cur_dir.parent
    _list(update, context)

def _select(update, context):
    global cur_dir
    fpath = str(update.message.text).split()
    # fpath[0] : /select
    # fpath[1] : destination
    flist = [str(x) for x in cur_dir.iterdir() if x.is_dir()]

    for item in flist:
        if fpath[1] in item:
            cur_dir = Path(item)
            cur_dir = cur_dir.resolve()
            break

def _send(update, context):
    global cur_dir
    fpath = str(update.message.text).split()
    # fpath[0] : /send
    # fpath[1] : target file
    flist = [str(x) for x in cur_dir.iterdir() if not x.is_dir()]

    for item in flist:
        if fpath[1] in item:
            f = open(item, "rb")
            context.bot.send_document(chat_id=update.message.chat_id, document=f)
            break

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("list", _list))
    dp.add_handler(CommandHandler("parent", _parent))
    dp.add_handler(CommandHandler("select", _select))
    dp.add_handler(CommandHandler("send", _send))
    #dp.add_handler(CommandHandler("id", id))
    #dp.add_handler(CommandHandler("pw", pw))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, ids))

    # log all errors
    dp.add_error_handler(error)

    updater.bot.send_message(1235556245, 'abcd')
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()