import telebot
import time 

with open("keys/api.key") as f:
    api = f.read()

API_TOKEN = api

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler()
def handle_dialog(message):
    bot.send_message(message.chat.id, "Я пока не понимаю человеческую речь, только команды.")


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет, я ваш ассистент July!\nЧем могу помочь?")

@bot.message_handler(commands=['time'])
def handle_time(message):
    bot.send_message(message.chat.id, f"Точное время по Гринвичу: {time.time()}")


bot.polling()