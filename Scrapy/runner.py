from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from time import sleep


settings = get_project_settings()
process = CrawlerProcess(settings)

for spider_name in process.spider_loader.list():
    print(spider_name)
    process.crawl(spider_name, query="dvh")

process.start()

sleep(20 * 60)