import json
from modules.notify import *

SETTINGS_FILE = 'settings.json'

def main():
    path = ''
    token = ''
    telegram_id = None

    with open(SETTINGS_FILE) as json_file:
        settings = json.load(json_file)
        path = settings['path']
        token = settings['token']
        telegram_id = settings['telegram_id']
        
    notify_service = NotifyService(path, token, telegram_id)
    notify_service.start()

if __name__ == '__main__':
    main()


