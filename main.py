import os
import time
import logging
#import dotenv для локального запуска бота
import requests
import telegram


def request_cheked_work(last_response_time):
    timestamp = {
        "timestamp": last_response_time
    }
    response = requests.get(url, params=timestamp, headers=headers)
    response.raise_for_status()
    return response.json()


def send_message(last_response):
    response_result = last_response['new_attempts'][0]
    title = response_result['lesson_title']
    url = response_result['lesson_url']
    if response_result['is_negative']:
        bot.send_message(chat_id=telegram_chat_id,
                         text=f'У вас проверили работу "{title}" \n К сожалению, в работе нашлись ошибки.\n https://dvmn.org{url}')
    else:
        bot.send_message(chat_id=telegram_chat_id,
                         text=f'У вас проверили работу "{title}" \n Преподавателю всё понравилось, можно приступать к следующему уроку!\n https://dvmn.org{url}')


if __name__ == '__main__':
    #dotenv.load_dotenv('.env')  для локального запуска бота
    devman_token = os.environ['DEVMAN_TOKEN']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token=telegram_token)
    url = 'https://dvmn.org/api/long_polling/'
    headers = {"Authorization": "Token {}".format(devman_token)}
    timestamp = None
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Произошло какое-то событие. Всё идёт по плану.')
    while True:
        try:
            response = request_cheked_work(timestamp)
            if response["status"] == "timeout":
                timestamp = response["timestamp_to_request"]
            else:
                timestamp = response["last_attempt_timestamp"]
                send_message(response)
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            time.sleep(60)
