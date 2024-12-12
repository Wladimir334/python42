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






def parse_html(html: str):
    total = []
    soup: Bs = Bs(html, 'html.parser')

    names = soup.find_all(class_="name_item")
    for name in names:
        name1 = str(name.text)

        print(f'{name1}')

    prices = soup.find_all(class_='price')
    for price in prices:
        price1 = price.text

        print(f'{name1} - {price1}')







    pass



URL = "https://parsinger.ru/html/index1_page_1.html"
html = get_html(URL)
if html:
    parse_html(html)


# title = title.encode('latini').decode('utf-8')