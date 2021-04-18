import logging
import os
import sys
import time

import requests
import telegram
from dotenv import load_dotenv

load_dotenv()


PRAKTIKUM_TOKEN = os.environ.get("PRAKTIKUM_TOKEN")
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s, %(levelname)s, %(name)s, %(message)s',
    stream=sys.stdout
)


def parse_homework_status(homework):

    homework_name = homework.get('homework_name')
    homework_status = homework.get('status')
    if homework_status is None:
        verdict = 'Неверный ответ сервера.'
    elif homework_status == 'rejected':
        verdict = 'К сожалению в работе нашлись ошибки.'
    elif homework_status == 'approved':
        verdict = ('Ревьюеру всё понравилось, '
                   'можно приступать к следующему уроку.')
    else:
        verdict = 'Неизвестный статус.'
    return f'У вас проверили работу "{homework_name}"!\n\n{verdict}'

# def parse_homework_status(homework):

#     homework_name = homework.get('homework_name')
#     homework_status = homework.get('status')
#     var_dict = {'rejected': True,
#                 'approved': True,
#                 'reviewing': True
#                 }
#     approved = var_dict.get(homework_status)
#     reviewing = var_dict.get(homework_status)
#     if approved is None or reviewing is None or homework_name is None:
#         return 'Неверный ответ сервера'
#     if approved:
#         verdict = ('Ревьюеру всё понравилось, '
#                    'можно приступать к следующему уроку.')
#     elif reviewing:
#         verdict = 'Работа взята в ревью.'
#     else:
#         verdict = 'К сожалению в работе нашлись ошибки.'
#     return f'У вас проверили работу "{homework_name}"!\n\n{verdict}'


def get_homework_statuses(current_timestamp):

    if current_timestamp is None:
        current_timestamp = int(time.time())
    url = 'https://praktikum.yandex.ru/api/user_api/homework_statuses/'
    headers = {'Authorization': f'OAuth {PRAKTIKUM_TOKEN}'}
    params = {'from_date': current_timestamp}
    homework_statuses = requests.get(url, headers=headers, params=params)
    return homework_statuses.json()


def send_message(message, bot_client):

    return bot_client.send_message(chat_id=CHAT_ID, text=message)


def main():
    bot_client = telegram.Bot(token=TELEGRAM_TOKEN)
    current_timestamp = int(time.time())

    while True:
        try:
            new_homework = get_homework_statuses(current_timestamp)
            if new_homework.get('homeworks'):
                send_message(parse_homework_status(
                    new_homework.get('homeworks')[0]), bot_client)
            current_timestamp = new_homework.get(
                'current_date',
                current_timestamp,
            )
            time.sleep(1100)

        except Exception as e:
            logging.error(f'Бот столкнулся с ошибкой: {e}')
            time.sleep(5)


if __name__ == '__main__':
    main()
