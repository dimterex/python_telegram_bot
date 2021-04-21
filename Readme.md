# Telegram-bot & watchdog

Описание:
- Скрипт для отслеживания удаления/создания/измнение/перемещения файлов внутри папки и оповещение с помощью telegram-бота.

Конфигурация:
```json
{
    "token": "token",
    "telegram_id": 123456789,
    "path": "."
}
```
* token - token telegram-бота.
* telegram_id - идентификатор учетной записи telegram.
* path - путь для отслеживания изменений.

Используемые библиотеки:
* watchdog
* python-telegram-bot
