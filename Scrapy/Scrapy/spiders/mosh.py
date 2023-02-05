import scrapy
from datetime import datetime
from locale import setlocale, LC_TIME


# NOTE: YOU NEED TO HAVE "ru_RU.UTF-8" LOCALE ON YOUR MACHINE
setlocale(LC_TIME, "ru_RU.UTF-8")


class Mosh(scrapy.Spider):
    name = "mosh"
    allowed_domains = ["mos.olimpiada.ru"]
    start_urls = ["https://mos.olimpiada.ru/news?count=0"]
    
    def parse(self, response):
        for news_item in response.css(".news_item"):
            date = news_item.css(".date::text").get()
            if len(date.split()) != 3:
                date += f" {datetime.now().year}"
                
            yield {
                "date": datetime.strptime(date, "%d %B %Y"),
                "title": news_item.css("a.name::text").get(),
                "link": "mos.olimpiada.ru" + news_item.css("a.name::attr(href)").get(),
                "description": ''
                }
