import requests
from random import randint

def get_image_link(url: str) -> str:
    resp = requests.get(url)
    data = resp.json()
    link = data.get("message")

    return link


def download_image(url: str) -> None:
    resp = requests.get(url)
    image = resp.content
    with open("image.jpg", "wb") as f:
        f.write(image)



#   /api/breeds - PATH-param ( параметры пути)
api_url = "https://dog.ceo/api/breeds/image/random"
link = get_image_link(url=api_url)
download_image(url=link)




