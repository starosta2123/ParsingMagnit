import datetime
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def collect_data(city_code='2209'):
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    ua = UserAgent()

#Словарь для заголовков!
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }

    cookies = {
        'mg_geo_id': f'{city_code}'
    }

#Отправляем запрос на сайт!

    response = requests.get(url='https://magnit.ru/promo/', headers=headers, cookies=cookies)

#Сохраняем результат
    with open(f'file.html', 'w', encoding="UTF-8") as file:
        file.write(response.text)


def main():
    collect_data(city_code='2209')


if __name__ == '__main__':
    main()
