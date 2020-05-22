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
def go(update, context):
    update.message.reply_text('아이디와 비밀번호를 입력해 주세요. ex) /start id pw')

def start(update, context):
    """Send a message when the command /start is issued."""
    info = update.message.text
    info_1 = info.split(' ')
    print(info_1)
    idi = collection.find_one({"id" : {"$eq":info_1[1]}})
    if idi != None:
        print(idi["id"])
    else:
        collection.insert_one({'id': info_1[1]})
        print("hi")

    idp = collection.find_one({"pw" : {"$eq":info_1[2]}})
    if idp != None:
        print(idp["pw"])
    else:
        collection.insert_one({'pw': info_1[2]})
        print("ho")


def echo(update, context):
    """Echo the user message."""
    print(update.message.chat_id)
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def _list(update, context):
    update.message.reply_text(collection.find_one({'내용'}))

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
    dp.add_handler(CommandHandler("go", go))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("list", _list))
    dp.add_handler(CommandHandler("parent", _parent))
    dp.add_handler(CommandHandler("select", _select))
    dp.add_handler(CommandHandler("send", _send))
    #dp.add_handler(CommandHandler("id", id))
    #dp.add_handler(CommandHandler("pw", pw))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    updater.bot.send_message(1235556245, '111')
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()