import os
import dotenv
import time
import requests
import telegram


def request_cheked_work(last_response_time):
    timestamp = "timestamp={}".format(last_response_time)
    response = requests.get(url, params=timestamp, headers=headers)
    response.raise_for_status()
    return response.json()


def send_message(last_response):
    title = last_response['new_attempts'][0]['lesson_title']
    url = last_response['new_attempts'][0]['lesson_url']
    if last_response['new_attempts'][0]['is_negative'] is True:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID,
                         text=f'У вас проверили работу "{title}" \n К сожалению, в работе нашлись ошибки.\n https://dvmn.org{url}')
    else:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID,
                         text=f'У вас проверили работу "{title}" \n Преподавателю всё понравилось, можно приступать к следующему уроку!\n https://dvmn.org{url}')


if __name__ == '__main__':
    dotenv.load_dotenv('.env')

    DEVMAN_TOKEN = os.environ['DEVMAN_TOKEN']
    TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
    TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    url = 'https://dvmn.org/api/long_polling/'
    headers = {"Authorization": "Token {}".format(DEVMAN_TOKEN)}

    try:
        timestamp = None
        while True:
            response = request_cheked_work(timestamp)
            if response["status"] == "timeout":
                timestamp = response["timestamp_to_request"]
            else:
                timestamp = response["last_attempt_timestamp"]
                send_message(response)

    except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
        time.sleep(60)
        pass
