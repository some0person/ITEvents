import scrapy


class Vosh(scrapy.Spider):
    name = "vosh"
    allowed_domains = ["vos.olimpiada.ru"]
    start_urls = ["https://vos.olimpiada.ru/news/count/-1?subject=all"]
    
    def parse(self, response):
        for element in response.xpath("//div[@class='div_main_block']//tr"):
            if element.css("a.news_headline::text").get():
                yield {
                    "date": element.css("span.date::text").get(),
                    "title": element.css("a.news_headline::text").get(),
                    "link": "vos.olimpiada.ru" + element.css("a.news_headline::attr(href)").get()}