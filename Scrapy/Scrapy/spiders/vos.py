import scrapy
from datetime import datetime


class Vosh(scrapy.Spider):
    name = "vos"
    allowed_domains = ["vos.olimpiada.ru"]
    start_urls = ["https://vos.olimpiada.ru/news/count/-1?subject=all"]
    
    def parse(self, response):
        for element in response.xpath("//div[@class='div_main_block']//tr"):
            if element.css("a.news_headline::text").get():
                yield {
                    "date": datetime.strptime(element.css("span.date::text").get(), "%d.%m.%Y"),
                    "title": element.css("a.news_headline::text").get(),
                    "link": "vos.olimpiada.ru" + element.css("a.news_headline::attr(href)").get(),
                    "description": '',
                    "source": "Всероссийская олимпиада школьников"
                    }