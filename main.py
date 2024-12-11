import telebot

with open("keys/api.key") as f:
    api = f.read()

API_TOKEN = api

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет, я ваш телеграм-бот!")

bot.polling()