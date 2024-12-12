from functions import *

def warning_message(message):
    return f"Я пока не понимаю человеческую речь, только команды"

def helps(message, cmd_list):
    return f"Список команд: {cmd_list}"

def hello(message, cmd_list):
    return f"Привет, я ваш ассистент July!\nЧем могу помочь?\n {cmd_list}"

def sidereal_timing(message):
    return f"Звёздное время по Гринвичу: {current_sidereal_time()}"