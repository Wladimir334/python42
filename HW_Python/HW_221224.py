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






def parse_html(html: str) -> str:
    soup: Bs = Bs(html, 'html.parser')

    pagins = soup.find('div', class_="pagen").text.split()
    left_pagins = soup.find('div', class_="nav_menu").text
    left_pagins_ru = left_pagins.encode('latin1').decode('utf-8')
    left = soup.find('div', 'a', class_="nav_menu")

    print(f'\n{pagins}, \n{left_pagins_ru}')

    left_links = soup.find('div', class_="nav_menu")
    url_left = left_links.find_all('a')
    for item in url_left:
        left_url = item.get('href')
        print('\nЛевые ссылки: ' + left_url)


    central_pagins = soup.find('div', class_="pagen")
    all_central_pagins = central_pagins.find_all('a')
    for link in all_central_pagins:
        central_url = link.get('href')
        print('\nЦентральные ссылки: ' + central_url)





URL = "https://parsinger.ru/html/index1_page_1.html"
html = get_html(URL)
if html:
    parse_html(html)