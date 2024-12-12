from functions import *
from commands import *
from classes import *

import telebot

with open("keys/api.key") as f:
    API_TOKEN = f.read()

ComandList = """
/help - справка по командам
/start - перезапуск бота
/stime - координаты звёздного времени
"""

bot = MyBot(API_TOKEN, ComandList)

bot.command('start', hello, bot.cmd_list)
bot.command('help', helps, bot.cmd_list)
bot.command('stime', sidereal_timing)
bot.dialogue(warning_message)

bot.polling()