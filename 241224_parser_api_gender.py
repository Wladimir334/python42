import requests

# ? - отделят домен от  QWERY-параметров
# name=misha = QWERY-param (параметр запроса)
# mvideo.ru/prodeucts?brand=samsung&model=galaxy&price_from=10000&price_to=40000

def get_gender_name(name: str) -> dict:
    params = {
        "name": name
    }
    url = f"https://api.genderize.io/"
    response = requests.get(url, params=params)
    data = response.json()
    print(data)

def parse_gender_name(name: dict) -> None:
    pass



get_gender_name(name="Alena")



# print(requests.get(url).json())

