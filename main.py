import time
from urllib.parse import urljoin

import requests
import telegram


def main():
    timestamp = time.time()

    headers = {
        'Authorization': 'Token be179ef94a5f2312e3530c418f1c5efda27cd2ec'
        }
    params = {
        "timestamp": timestamp
        }
    url = 'https://dvmn.org/api/long_polling/'

    while True:
        try:
            response = requests.get(url, headers=headers, params=params, timeout=100)
            response.raise_for_status()

        except (
            requests.exceptions.ConnectionError,
        ) as e:
            print(f"restart cause: {e}")
            time.sleep(20)
        except requests.exceptions.ReadTimeout:
            pass

        else:
            answer = response.json()        
            if answer['status'] == 'timeout':
                params['timestamp'] = answer['timestamp_to_request']

            if answer['status'] == 'found':
                params['timestamp'] = answer['last_attempt_timestamp']
                send_message(answer, bot, '@Graph_Zero0_bot')


def send_message(answer, bot, chat_id):
    new_attempts = answer['new_attempts'][0]
    lesson_title = new_attempts['lesson_title']
    lesson_url = urljoin('https://dvmn.org', new_attempts['lesson_url'])

    if new_attempts['is_negative']:
        teacher_decision = f'Your work "{lesson_title}"\n{lesson_url}has been checked.\nUnfortunately, some mistakes were found'

    else:
        teacher_decision = f'Your work "{lesson_title}"\n{lesson_url}has been checked.\nTeacher liked everything, you can start the next lesson'

    bot.send_message(chat_id, teacher_decision)
    
    
if __name__ == '__main__':
    bot = telegram.Bot('5224554467:AAEVXCNK0Me5AUI1HLDKzwPg4oH6WOAbNN0')
    main()
    