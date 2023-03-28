# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from os import environ
from datetime import datetime
import psycopg2


class ScrapyPipeline:
    def __init__(self):
        hostname = environ["URL_DB"]
        username = environ["POSTGRES_USER"]
        password = environ["POSTGRES_PASSWORD"]
        database = environ["POSTGRES_DB"]
        
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()
                
    def process_item(self, item, spider):
        self.cur.execute(f"""SELECT link FROM news WHERE link='{item["link"]}'""")
        if self.cur.fetchone():
            return item
        self.cur.execute("""
                         INSERT INTO news (date, title, link, description, source, date_updated) VALUES (%s, %s, %s, %s, %s, %s)
                         """, (str(item["date"]), item["title"], item["link"], item["description"], item["source"], str(datetime.now())))
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

