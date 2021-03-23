import logging
import os
import time

import dotenv
import requests
import telegram

from handler import TelegramBotHandler


def request_cheked_work(last_response_time, devman_token):
    url = 'https://dvmn.org/api/long_polling/'
    headers = {"Authorization": "Token {}".format(devman_token)}
    timestamp = {
        "timestamp": last_response_time
    }
    response = requests.get(url, params=timestamp, headers=headers)
    response.raise_for_status()
    return response.json()


def send_message(last_response, bot, telegram_chat_id):
    response_result = last_response['new_attempts'][0]
    title = response_result['lesson_title']
    url = response_result['lesson_url']
    if response_result['is_negative']:
        bot.send_message(chat_id=telegram_chat_id,
                         text=f'У вас проверили работу "{title}" \n К сожалению, в работе нашлись ошибки.\n https://dvmn.org{url}')
    else:
        bot.send_message(chat_id=telegram_chat_id,
                         text=f'У вас проверили работу "{title}" \n Преподавателю всё понравилось, можно приступать к следующему уроку!\n https://dvmn.org{url}')


def main():
    dotenv.load_dotenv('.env')
    devman_token = os.environ['DEVMAN_TOKEN']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token=telegram_token)

    timestamp = None
    logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(format="%(process)d %(levelname)s %(message)s")

    logger = logging.getLogger("logger")
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramBotHandler(telegram_token, telegram_chat_id))
    logger.info("Бот запущен")

    while True:
        try:
            response = request_cheked_work(timestamp, devman_token)
            if response["status"] == "timeout":
                timestamp = response["timestamp_to_request"]
            else:
                timestamp = response["last_attempt_timestamp"]
                send_message(response, bot, telegram_chat_id)
        except requests.exceptions.ReadTimeout as read_timeout:
            logger.error("Бот упал с ошибкой:")
            logger.error(read_timeout, exc_info=True)
            pass
        except requests.exceptions.ConnectionError as connection_error:
            logger.error("Бот упал с ошибкой:")
            logger.error(connection_error, exc_info=True)
            time.sleep(60)


if __name__ == '__main__':
    main()
