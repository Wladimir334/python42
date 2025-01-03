from http.client import responses
import json
from textwrap import indent

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

    main_table = soup.find('div', {"id" : "content-left"})
    tables = main_table.find('div', class_="weather-short").find_all('table')

    # for table in main_table:

    pass

    # weather_info = {}
    # day = soup.find('div', class_="dates short-d").text
    # weather_info[day] = {}
    # table = soup.find('div', class_="weather-short").find("table")
    # table_rows = table.find_all('tr')
    # for row in table_rows:
    #     weather_day = row.find('td', class_="weather-day").text
    #     weather_info[day][weather_day] = {}
    #     weather_temperature = row.find('td', class_="weather-temperature").text
    #     weather_type = row.find('div', class_="wi")['title']
    #     weather_feeling = row.find('td', class_="weather-feeling").text
    #     weather_probability = row.find('td', class_="weather-probability").text
    #
    #     weather_info[day][weather_day]["weather-temperature"] = weather_temperature
    #     weather_info[day][weather_day]["weather_type"] = weather_type
    #     weather_info[day][weather_day]["weather-feeling"] = weather_feeling
    #     weather_info[day][weather_day]["weather-probability"] = weather_probability
    # return weather_info


# def write_data_to_json(data: dict) -> None:
#     with open('weather_week.json', "w") as file:
#         json.dump(data, file, indent=2, ensure_ascii=False)




URL = "https://world-weather.ru/pogoda/russia/saint_petersburg/7days/"
html = get_html(url=URL)
if html:
    data = get_weather_from_week(html)
    # write_data_to_json(data)
