from flask import Flask, render_template


# =============== !TEMPORARY TESTING DATA! ===============
from datetime import datetime
news = [
    {
    'id': 0,
    'date': datetime(2023, 2, 24, 15, 56, 29, 188963),
    'title': 'Article 0',
    'link': 'https://example.com/',
    'description': 'Example article descrition 0',
    'date_updated': datetime.now()
    },
    {
    'id': 1,
    'date': datetime(2023, 2, 24, 15, 58, 36, 194402),
    'title': 'Article 1',
    'link': 'https://example.com/',
    'description': 'Example article descrition 1',
    'date_updated': datetime.now()
    }
]
# =============== !TEMPORARY TESTING DATA! ===============


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', news=news)