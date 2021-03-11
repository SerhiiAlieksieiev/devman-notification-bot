# Devman notification bot

Бот позволяет отправлять уведомления о проверке работ ученикам Devman. Использует Devman API и Telegram.
 
### Запуск
1. Создайте телеграм-бота - [Гайд по созданию телеграм-бота](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
2. Скачайте репозиторий командой
  
	`git clone https://github.com/SerhiiAlieksieiev/devman-notification-bot.git`
3. Сделайте виртуальное окружение командой
 
 	`python -m venv --copies /полный/путь/до/папки/виртуального/окружения `
4. Установите зависимости  командой 

	`py -m pip install -r requirements.txt`

5. Запустите скрипт командой 

	`python main.py`
 
### Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом  с `main.py` и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Доступны 3 переменные:
- `DEVMAN_TOKEN` — персональный токен, можно найти [здесь](https://dvmn.org/api/docs/).
- `TELEGRAM_TOKEN` — токен вашего бота, можно узнать у [BotFarther](https://telegram.me/BotFather)
- `TELEGRAM_CHAT_ID` — персональный chat id, можно узнать у [userinfobot](https://telegram.me/userinfobot)
