FROM python:3-alpine

RUN mkdir -p /usr/src/flask
WORKDIR /usr/src/flask

RUN pip3 install --upgrade pip
RUN pip3 install flask psycopg2-binary
COPY . .

CMD ["python3", "run.py"]