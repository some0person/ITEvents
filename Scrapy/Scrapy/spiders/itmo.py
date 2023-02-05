import scrapy
from json import loads
from datetime import datetime


class Itmo(scrapy.Spider):
    name = "itmo"
    allowed_domains = ["olymp.itmo.ru"]
    start_urls = ["https://olymp.itmo.ru/api/news?languageCode=ru"]

    def parse(self, response):
        for element in loads(response.text):
            yield {
                "date": datetime.strptime(element["dateCreated"].split('T')[0], "%Y-%m-%d"),
                "title": element["name"],
                "link": f"olymp.itmo.ru/s/{element['id']}",
                "description": ''
                }
