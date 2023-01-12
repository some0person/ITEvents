import scrapy


class Olimpiadaru(scrapy.Spider):
    name = 'olimpiadaru'
    allowed_domains = ['mos.olimpiada.ru']
    start_urls = ['https://olimpiada.ru/news']
    
    def parse(self, response):
        news = response.xpath("/html/body/div/div[3]/div[1]")
        for n in news:
            for date in n.css("h2::text").getall():
                names = n.css("a::text").getall(),
                links = n.css("a::attr(href)").extract()
                print(11111111111111111, names[0])
                for x in range(len(names[0])):
                    yield {"date": date,
                           "name": names[x],
                           "link": links[x]}



