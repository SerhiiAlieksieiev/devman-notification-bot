from datetime import datetime

import requests
import telegram

from settings import DEVMAN_TOKEN, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


def request_cheked_work(last_response_time):
    timestamp = "timestamp={}".format(last_response_time)
    response = requests.get(url, params=timestamp, headers=headers)
    response.raise_for_status()
    return response.json()

def send_positive_message(last_response):
    bot.send_message(chat_id=chat_id,
                     text='У вас проверили работу "{}" \n К сожалению, в работе нашлись ошибки.\n https://dvmn.org{}'.format(
                         last_response['new_attempts'][0]['lesson_title'],
                         last_response['new_attempts'][0]['lesson_url']))

def send_negative_message(last_response):
    bot.send_message(chat_id=chat_id,
                     text='У вас проверили работу "{}" \n Преподавателю всё понравилось, можно приступать к следующему уроку!\n https://dvmn.org{}'.format(
                         last_response['new_attempts'][0]['lesson_title'],
                         last_response['new_attempts'][0]['lesson_url']))

if __name__ == '__main__':
    chat_id = TELEGRAM_CHAT_ID
    telegram_token = TELEGRAM_TOKEN
    devman_token = DEVMAN_TOKEN
    bot = telegram.Bot(token=telegram_token)
    url = 'https://dvmn.org/api/long_polling/'
    headers = {"Authorization": "Token {}".format(devman_token)}

    try:
        last_response = request_cheked_work(datetime.now().timestamp())
        while True:
            if last_response["status"] == "timeout":
                response = request_cheked_work(last_response["timestamp_to_request"])
                last_response = response
            else:
                if last_response['new_attempts'][0]['is_negative'] == True:
                    send_positive_message(last_response)
                else:
                    send_negative_message(last_response)
                response = request_cheked_work(last_response["last_attempt_timestamp"])
                last_response = response
    except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
        pass
