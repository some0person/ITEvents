import json
import requests


def placeholder(date, name, description, link):
    with open("result.txt", "a") as file:
        file.write(f"{date} | {name} | {description} | {link}\n")


URL = "https://olymp.itmo.ru/api/news?languageCode=ru"

for item in json.loads(requests.get(URL).text):
    placeholder(item["dateCreated"].split('T')[0], item["name"], '', f"olymp.itmo.ru/s/{item['id']}")
