import scrapy
from datetime import datetime


class Predprof(scrapy.Spider):
    name = "predprof"
    allowed_domains = ["predprof.olimpiada.ru"]
    start_urls = ["https://predprof.olimpiada.ru/news"]

    def parse(self, response):
        allNews = response.css("span.data_news")
        
        for x in range(len(allNews)):
            try:
                yield {
                    "date": datetime.strptime(allNews[x].css("b::text").get(), "%d.%m.%Y"),
                    "title": allNews[x].css("a::text").get(),
                    "link": "predprof.olimpiada.ru" + allNews[x].css('a').attrib["href"],
                    "description": response.xpath(f"//div/div/div/p[{x + 1}]/span/text()").extract()[-1]
                    }
            except IndexError:
                pass