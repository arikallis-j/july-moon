from functions import *
from commands import *
from classes import *

import telebot

with open("keys/api.key") as f:
    API_TOKEN = f.read()

ComandList = """
Команды:
/help - справка по командам
/start - перезапуск бота
/stime - координаты звёздного времени
/arxivnow - подборка статей из архива [astro-ph.HE],\nопубликованные сегодня

Рассылки:
/arxiv - подборка статей из архива [astro-ph.HE] за сутки в 12:00
/goodmorning - доброе утро в 11:00
"""

bot = MyBot(API_TOKEN, ComandList)

bot.command('start', hello, bot.cmd_list)
bot.command('help', helps, bot.cmd_list)
bot.command('stime', sidereal_timing)
bot.command('arxivnow', send_daily_articles, parse_mode=article_parse)
bot.command('goodmorningnow', goodmorning)

bot.daily_task('goodmorning', goodmorning, timer="11:00")
bot.daily_task('arxiv', send_daily_articles, timer="12:00", parse_mode=article_parse)
bot.dialogue(warning_message)
bot.polling()
