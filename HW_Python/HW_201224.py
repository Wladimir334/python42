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
    total = {}
    soup: Bs = Bs(html, 'html.parser')


    name1 = soup.find('a', class_="name_item", href="watch/1/1_1.html").text
    name2 = soup.find('a', class_="name_item", href="watch/1/1_2.html").text
    name3 = soup.find('a', class_="name_item", href="watch/1/1_3.html").text
    name4 = soup.find('a', class_="name_item", href="watch/1/1_4.html").text
    name5 = soup.find('a', class_="name_item", href="watch/1/1_5.html").text
    name6 = soup.find('a', class_="name_item", href="watch/1/1_6.html").text
    name7 = soup.find('a', class_="name_item", href="watch/1/1_7.html").text
    name8 = soup.find('a', class_="name_item", href="watch/1/1_8.html").text

    prices = soup.find_all('p', class_="price")

    for price in prices:
        price1 = price.find('p', class_="price")

        print(f'{price1}')









    # total = {
    #     name1:
    # }



    pass



URL = "https://parsinger.ru/html/index1_page_1.html"
html = get_html(URL)
if html:
    parse_html(html)


# title = title.encode('latini').decode('utf-8')