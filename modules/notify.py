from modules.folder_watcher import *
from modules.telegram_bot import *
from watchdog.events import PatternMatchingEventHandler

class NotifyService():

    def __init__(self, path, token, telegram_id):
        self.folder_wather = FolderWather(path)
        self.bot = TelegramBot(token, telegram_id)

    def start(self):

        try:
            self.bot.start()
            self.folder_wather.start(self.on_created, self.on_deleted, self.on_modified, self.on_moved)
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.folder_wather.stop()
            self.bot.stop()

    def stop(self):
        self.folder_wather.stop()
        self.bot.stop()

    def on_created(self, event):
        self.bot.send_message(f"Добавлен: {event.src_path}")

    def on_deleted(self, event):
        self.bot.send_message(f"Удален: {event.src_path}")

    def on_modified(self, event):
        self.bot.send_message(f"Изменен: {event.src_path}")

    def on_moved(self, event):
        self.bot.send_message(f"Перемещен: {event.src_path} -> {event.dest_path}")

