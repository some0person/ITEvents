import psycopg2
from os import environ


class News:
    def __init__(self):
        hostname = environ["URL_DB"]
        username = environ["POSTGRES_USER"]
        password = environ["POSTGRES_PASSWORD"]
        database = environ["POSTGRES_DB"]
        
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def getNews(self, start, end, sortby="id", reverse=False, filtercell="title", filterarg=''):
        if reverse:
            reverse = "DESC"
        else:
            reverse = "ASC"
        self.cur.execute(f"SELECT * FROM (SELECT id,source,title,link,description,date,row_number() \
                           OVER (ORDER BY {sortby} {reverse}) AS rn FROM news WHERE {filtercell} \
                           LIKE '%{filterarg}%') sub WHERE rn>='{start}' AND rn<='{end}' ORDER By rn DESC")
        data = [{"id": element[0], "source": element[1],
                "title": element[2], "link": element[3],
                "description": element[4], "date": element[4]} for element in self.cur.fetchall()]

        return data[::-1]