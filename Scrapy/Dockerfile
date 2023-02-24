FROM python:3-alpine

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

RUN pip3 install --upgrade pip
RUN pip3 install psycopg2-binary Scrapy
COPY . .

CMD ["python3", "runner.py"]