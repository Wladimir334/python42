from http.client import responses

import requests
from bs4 import BeautifulSoup
from urllib3 import request


def get_links_dogs(url:str) -> str:
    resp = requests.get(url)
    data = resp.json()

    for i in range(1, 31):
        url = f"https://images.dog.ceo/breeds/briard/n02105251_80{i}.jpg"
        req = request.get(url=url)
        response = req.content

        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            print(f"Downloaded {i} of 31")

def main():
    get_links_dogs()

if __name__ == '__main__':
    main()

# api_url = "https://dog.ceo/api/breeds/image/random"