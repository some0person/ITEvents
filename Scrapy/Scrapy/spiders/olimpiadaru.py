import scrapy


class Olimpiadaru(scrapy.Spider):
    name = 'olimpiadaru'
    allowed_domains = ['olimpiada.ru']
    start_urls = ['https://olimpiada.ru/news']
    
    def parse(self, response):
        pass