import scrapy
from json import loads


class Itmo(scrapy.Spider):
    name = "itmo"
    allowed_domains = ["olymp.itmo.ru"]
    start_urls = ["https://olymp.itmo.ru/api/news?languageCode=ru"]

    def parse(self, response):
        for element in loads(response.text):
            yield {
                "date": element["dateCreated"],
                "title": element["name"],
                "description": '',
                "link": f"olymp.itmo.ru/s/{element['id']}"
                }
