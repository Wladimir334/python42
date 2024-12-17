# import json

import requests
from bs4 import BeautifulSoup as Bs
from requests.exceptions import ConnectionError



def get_html(url: str) -> str:
    try:
        response = requests.get(url)
        status = response.status_code
        if status != 200 and str(status)[0] !=3:
            print(f'Ошибка запроса. Код ответа -  {status}')
            return None
        print(f"Код ответа - {status}")
        html = response.text
        return html
    except ConnectionError as error:
        print('Нет ответа с сервера')
        print(error)
        return None


def parse_html(html: str) -> dict:

    soup: Bs = Bs(html, 'html.parser')

    item_card = soup.find('div', class_="item_card")

    names = item_card.find_all('a', class_='name_item')

    for name in names:
        name1 = name.text.encode('latin1').decode('utf-8')
        print(name1)


    prices = item_card.find_all('p', class_="price")

    for price in prices:
        price1 = price.text.encode('latin1').decode('utf-8')
        print(price1)



URL = "https://parsinger.ru/html/index1_page_1.html"
html = get_html(URL)
if html:
    parse_html(html)

