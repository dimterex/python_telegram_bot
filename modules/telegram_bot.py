from telegram import Update, ForceReply, TelegramObject
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, PicklePersistence

class TelegramBot():
    def __init__(self, token, telegram_id):
        self.updater = Updater(token)
        self.telegram_id = telegram_id

    def start(self):
        self.updater.start_polling()

    def stop(self):
        self.updater.idle()

    def send_message(self, message):
        self.updater.bot.sendMessage(self.telegram_id, message)
