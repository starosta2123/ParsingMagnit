import datetime
from typing import Union

import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from fake_useragent import UserAgent


def collect_data(city_code='2209'):
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    ua = UserAgent()

#Heading Dictionary
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }

    cookies = {
        'mg_geo_id': f'{city_code}'
    }

#Sending a request to the site

    response = requests.get(url='https://magnit.ru/promo/', headers=headers, cookies=cookies)

#Save the result
    with open(f'index.html', 'w', encoding="UTF-8") as file:
        file.write(response.text)

    #with open('file.html') as file:
       # src = file.read()

  #  soup = BeautifulSoup (src, 'lxml')

  #  city = soup.find('a', class_ = 'header__contacts-link_city').text.strip()
   # print(city)




def main():
    collect_data(city_code='2209')


if __name__ == '__main__':
    main()
