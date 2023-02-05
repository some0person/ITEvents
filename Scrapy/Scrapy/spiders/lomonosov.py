import scrapy
from datetime import datetime


class Lomonosov(scrapy.Spider):
    name = "lomonosov"
    allowed_domains = ["olymp.msu.ru"]
    start_urls = ["https://olymp.msu.ru/rus/page/main/29/news/items"]

    def parse(self, response):
        URL = "https://olymp.msu.ru/rus/page/main/29/news/items"
        last_page = response.css("a.pagination__link.pagination__link--forward::attr(href)").get().split('=')[-1]
        for i in range(1, int(last_page) + 1):
            yield scrapy.Request(url=f"{URL}?page={i}", callback=self.parse_page)

    def parse_page(self, response):
        for news_item in response.css("article.blog-entry"):
            yield {
                "date": datetime.strptime(news_item.css("time.blog-entry__date::text").get(), "%d.%m.%Y"),
                "title": news_item.css("h2.blog-entry__heading::text").get(),
                "link": "olymp.msu.ru" + news_item.css("a.blog-entry__wrapper::attr(href)").get(),
                "description": news_item.css("p::text").get()
                }