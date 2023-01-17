import scrapy


class Mosh(scrapy.Spider):
    name = "mosh"
    allowed_domains = ["mos.olimpiada.ru"]
    start_urls = ["https://mos.olimpiada.ru/news?count=0"]
    
    def parse(self, response):
        for news_item in response.css(".news_item"):
            yield {"date": news_item.css(".date::text").get(),
                   "title": news_item.css("a.name::text").get(),
                   "link": "mos.olimpiada.ru" + news_item.css("a.name::attr(href)").get()}
