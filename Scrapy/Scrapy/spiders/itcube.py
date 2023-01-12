import scrapy


class Itcube(scrapy.Spider):
    name = 'itcube'
    allowed_domains = ['predprof.olimpiada.ru']
    start_urls = ['https://predprof.olimpiada.ru/news']

    def parse(self, response):
        allNews = response.css('span.data_news')
        for x in range(len(allNews)):
            try:
                yield {
                    'date': allNews[x].css('b::text').get(),
                    'link': 'https://predprof.olimpiada.ru' + allNews[x].css('a').attrib['href'],
                    'title': allNews[x].css('a::text').get(),
                    'description': response.xpath(f'//div/div/div/p[{x + 1}]/span/text()').extract()[-1]}
            except IndexError:
                pass