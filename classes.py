from functions import *

import telebot
import schedule
import threading
import yaml


class MyBot:
    def __init__(self, api, ComandList="ComandList"):
        self.bot = telebot.TeleBot(api)
        self.cmd_list = ComandList
        self.scheduler_thread = None

        with open("pre_db.yml", "r") as f:
            self.tasks = yaml.safe_load(f)['tasks']
    
    def command(self, name, func, *args, parse_mode='Markdown'):
        @self.bot.message_handler(commands=[name])
        def handle_command(message):
            self.bot.send_message(message.chat.id, func(message, *args), parse_mode=parse_mode)      

    def dialogue(self, func, *args, parse_mode='Markdown'):
        @self.bot.message_handler()
        def handle_dialogue(message):
            self.bot.send_message(message.chat.id, func(message, *args), parse_mode=parse_mode)

    def daily_task(self, name, func, *args, timer="08:00", interval=10, parse_mode='Markdown'):
        """Добавляет задачу в расписание и запускает поток для выполнения."""
        try:
            task_chat = self.tasks[name]
        except:
            self.tasks[name] = []
            task_chat = self.tasks[name]

        @self.bot.message_handler(commands=[name])
        def append_task(message):
            if len(task_chat)==0:
                task_chat.append(message.chat.id)
                self.bot.send_message(message.chat.id, f"Подписка на задачу {name}", parse_mode=parse_mode)

            else:
                is_chat = False
                for chat in task_chat:
                    if chat==message.chat.id:
                        is_chat = True
                        task_chat.remove(chat)
                        self.bot.send_message(message.chat.id, f"Вы отписались от {name}", parse_mode=parse_mode)
                if not(is_chat):
                    task_chat.append(message.chat.id)
                    self.bot.send_message(message.chat.id, f"Подписка на задачу {name}", parse_mode=parse_mode)
            with open("pre_db.yml", 'w') as f:
                yaml.dump({'tasks': self.tasks}, f)

        @self.bot.message_handler(commands=[f'{name}_ping'])
        def handle_task(chat):
            self.bot.send_message(chat.id, func(chat, *args), parse_mode=parse_mode)
            
        def task():
            for chat in task_chat:
                handle_task(chat)

        schedule.every().day.at(timer).do(task)
        
        def run_scheduler():
            while True:
                schedule.run_pending()
                time.sleep(1)

        if not self.scheduler_thread or not self.scheduler_thread.is_alive():
            self.scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
            self.scheduler_thread.start()

    def polling(self):
        self.bot.polling()

