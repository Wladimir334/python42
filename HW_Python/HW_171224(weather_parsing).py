from http.client import responses

import requests
from bs4 import BeautifulSoup as Bs
from requests.exceptions import ConnectionError

def get_html(url: str) -> str:
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers)
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




def get_weather_from_week(html: str) -> dict:
    soup = Bs(html, 'html.parser')

    weather_info = {}
    seven_days = soup.find('div', id="content-left").find_all('div', class_="weather-short")

    pass


URL = "https://world-weather.ru/pogoda/russia/saint_petersburg/7days/"
html = get_html(url=URL)
if html:
    get_weather_from_week(html)