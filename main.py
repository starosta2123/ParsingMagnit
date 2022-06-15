import datetime
from typing import Union
import csv
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from fake_useragent import UserAgent

#Get current date and UserAgent
def collect_data(city_code='2209'):
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    ua = UserAgent()

#Forming headers and cookies
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
 #   with open(f'index.html', 'w', encoding="UTF-8") as file:
 #       file.write(response.text)

 #   with open('index.html', encoding="UTF-8") as file:
 #      src = file.read()
    soup = BeautifulSoup(response.text, 'lxml')

#We find the city and collect all the cards with goods
    city = soup.find('a', class_ = 'header__contacts-link_city').text.strip()
    cards = soup.find_all('a', class_='card-sale_catalogue')
    #print(city, len(cards))

#Write headers to csv file
    with open(f'{city}_{cur_time}.csv','w') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                'Продукт',
                'Старая цена',
                'Новая цена',
                'Процент скидки',
                'Время акции'
            )
        )
#We collect the necessary information from the cards
    for card in cards:
        card_title = card.find('div', class_= 'card-sale__title').text.strip() #The product's name
        
#Check if there is a discount on the product. Is there any - we continue to collect information
        try:
            card_discount = card.find ('div', class_='card-sale__discount').text.strip()
        except AttributeError:
            continue

        card_price_old_integer = card.find('div', class_='label__price_old').find('span', class_='label__price-integer').text.strip()
        card_price_old_decimal = card.find('div', class_='label__price_old').find('span', class_='label__price-decimal').text.strip()
        card_old_price = f'{card_price_old_integer}.{card_price_old_decimal}'

        card_price_integer =  card.find('div', class_='label__price_new').find('span', class_='label__price-integer').text.strip()
        card_price_decimal =  card.find('div', class_='label__price_new').find('span', class_='label__price-decimal').text.strip()
        card_price = f'{card_price_integer}.{card_price_decimal}'

        card_sale_date = card.find('div', class_='card-sale__date').text.strip().replace('\n', ' ')
        print(card_sale_date)

#Adding all data to csv file
        with open(f'{city}_{cur_time}.csv', 'a') as file:
            writer = csv.writer(file)

            writer.writerow(
                (
                     card_title,
                     card_old_price,
                     card_price,
                     card_discount,
                     card_sale_date
                )
            )
        
        print(f'Файл {city}_{cur_time}.csv успешно записан!')


def main():
    collect_data(city_code='2209')


if __name__ == '__main__':
    main()
