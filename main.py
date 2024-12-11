import telebot
import time

def current_sidereal_time():
    # Получаем количество секунд с начала эпохи Unix
    seconds_since_epoch = time.time()

    # Время в юлианских днях с начала эпохи
    julian_days = seconds_since_epoch / 86400 + 2440587.5
    
    # Звёздное время в часах
    sidereal_time = (280.46061837 + 360.98564736629 * (julian_days - 2451545)) % 360
    
    # Преобразуем в часы, минуты, секунды
    hours = int(sidereal_time / 15 + 3) % 24
    minutes = int((sidereal_time % 15) * 4)
    seconds = int((((sidereal_time % 15) * 4) % 1) * 60)
    
    return f"{hours:02}:{minutes:02}:{seconds:02}"

with open("keys/api.key") as f:
    api = f.read()

API_TOKEN = api


ComandList = """
/help - справка по командам
/start - перезапуск бота
/time - координаты точного времени
"""

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help'])
def handle_time(message):
    bot.send_message(message.chat.id, f"Список команд: {ComandList}")


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, f"Привет, я ваш ассистент July!\nЧем могу помочь?\n{ComandList}")

@bot.message_handler(commands=['time'])
def handle_time(message):
    bot.send_message(message.chat.id, f"Звёздное время по Гринвичу: {current_sidereal_time()}")


@bot.message_handler()
def handle_dialog(message):
    bot.send_message(message.chat.id, "Я пока не понимаю человеческую речь, только команды.")


bot.polling()