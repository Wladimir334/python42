import requests
from bs4 import BeautifulSoup as Bs
import json

class Parser:
    def __init__(self, url):
        self.url = url
        self.data_weather = {}
        self.data_vacancies = []
        self.html = None

    def get_html(self):
        response = requests.get(self.url)
        self.html = response.text

        #return html

    def parse_html(self):
        self.get_html()
        soup = Bs(self.html, "parser.html")
        data = soup.find_all("table", class_="weather")
        self.data_weather = {"data": data}

    def  write_data_to_file(self):
        with open("file.txt", "w") as f:
            json.dump(self.data_weather, f, indent=2)

        #return data

parser_weather = Parser(url="www.weather.com")
parser_weather.parse_html()

# parser_weather = Parser(url="www.weather.com")
# html = parser_weather.get_html()
# data = parser_weather.parse_html(html)
