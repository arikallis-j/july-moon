from functions import *

import telebot

class MyBot:
    def __init__(self, api, ComandList="ComandList"):
        self.bot = telebot.TeleBot(api)
        self.cmd_list = ComandList
    
    def command(self, name, func, *args):
        @self.bot.message_handler(commands=[name])
        def handle_start(message):
            self.bot.send_message(message.chat.id, func(message, *args))

    def dialogue(self, func, *args):
        @self.bot.message_handler()
        def handle_start(message):
            self.bot.send_message(message.chat.id, func(message, *args))

    def polling(self):
        self.bot.polling()

