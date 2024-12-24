import requests

def get_vacancies_pages(url: str):
    area = 2
    per_page = 100
    text = "python"

    params = {
        "area": 2,
        "per_page": 100,
        "text": text
    }


    return data['pages'], data['found']


def get_data_page(url: str, page: int):
    params = {
        "area": 2,
        "per_page": 100,
        "page": page,
        "text": "python"
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    return data

def parse_page(data: dict):
    vacancies = {}
    items = data["items"]
    for i in items:
        vacancies[i["id"]] = i["name"]
    return vacancies



def main():
    vacancies = []
    url_api = "https://api.hh.ru/vacancies"
    pages, found = get_vacancies_pages(url=url_api)
    print(f"Найдено {found} вакансий")
    for i in range(1, pages+1):
        data_page = get_data_page(url=url_api, page=1)
        vacancies.append(parse_page(data_page))
    print(*vacancies, sep='\n')

# print(resp.status_code, resp.text)