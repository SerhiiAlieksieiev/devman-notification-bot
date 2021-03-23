# Devman notification bot

Бот позволяет отправлять уведомления о проверке работ ученикам Devman. Использует Devman API и Telegram.
 
###Локальный запуск
1. Создайте телеграм-бота - [Гайд по созданию телеграм-бота](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
2. Скачайте репозиторий командой
  
	`git clone https://github.com/SerhiiAlieksieiev/devman-notification-bot.git`
3. Сделайте виртуальное окружение командой
 
 	`python -m venv --copies /полный/путь/до/папки/виртуального/окружения `
4. Установите зависимости  командой 

	`py -m pip install -r requirements.txt`
5. Добавьте в начало кода `import dotenv`
   и в `def main():` `dotenv.load_dotenv('.env')`
   
6. Запустите скрипт командой 

	`python main.py`
 
### Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом  с `main.py` и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Доступны 3 переменные:
- `DEVMAN_TOKEN` — персональный токен, можно найти [здесь](https://dvmn.org/api/docs/).
- `TELEGRAM_TOKEN` — токен вашего бота, можно узнать у [BotFarther](https://telegram.me/BotFather)
- `TELEGRAM_CHAT_ID` — персональный chat id, можно узнать у [userinfobot](https://telegram.me/userinfobot)

### Деплой на Heroku
1. Создайте телеграм-бота - [Гайд по созданию телеграм-бота](https://core.telegram.org/bots#3-how-do-i-create-a-bot)

2. Зарегистрируйстесь на Heroku и создайте приложение

3. Опубликойте свой код на GitHub

4. Привяжите GitHub к аккаунту Heroku и нажмите Deploy Branch внизу страницы

5. Создайте [Procfile](https://devcenter.heroku.com/articles/procfile) с одной строчкой
	
	`bot: python3 main.py`

6. Добавьте переменные окружение во вкладке Settings на сайте Heroku.

### Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/referrals/eC72w2BASG9Zj3T7iMTSsxDbHXthCmJmeLKBNfwf/).