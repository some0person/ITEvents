from flask import Flask, render_template, request


# =============== !TEMPORARY TESTING DATA! ===============
from datetime import datetime
allowed_sorting_parameters = ('source', 'id', 'title', 'date', 'description', 'date_updated')
news_origin = []
for i in range(26):
    news_origin.append(
        {
        'source': f'Source {chr(122 - i)}',
        'id': i,
        'date': datetime(2023, 2, 24, 15, 56, 29, 188963),
        'title': f'Article {i}',
        'link': 'https://example.com/',
        'description': f'Example article descrition {i}',
        'date_updated': datetime.now()
        }
    )
# =============== !TEMPORARY TESTING DATA! ===============


app = Flask(__name__)


# @app.route('/', methods=['GET'], defaults={'uid': 'zero'})
@app.route('/', methods=['GET'])
def home():
    args = request.args
    sorting_arg, reverse_arg, per_page_arg, page_arg = args.get('sort'), 'reverse' in args, args.get('perpage', default='8'), args.get('p', default='0')
    page, per_page = int(page_arg) if page_arg.isdecimal() else 0, int(per_page_arg) if per_page_arg.isdecimal() and int(per_page_arg) >= 1 else 10

    # Should be replaced later with database functions
    if sorting_arg in allowed_sorting_parameters:
        news = sorted(news_origin, key=lambda x: x[sorting_arg], reverse=reverse_arg if reverse_arg in (True, False) else False)
    else:
        news = news_origin
    news_page = news[page * per_page:(page + 1) * per_page]
        
    # Pages usage examples:
    #   http://127.0.0.1:5000/?p=0&perpage=15   Page 0 with 15 articles on each
    #   http://127.0.0.1:5000/?p=5&perpage=2    Page 5 with 2 articles on each

    # Sorting examples:
    #   http://127.0.0.1:5000/?sort=source  Sorting by 'source'
    #   http://127.0.0.1:5000/?sort=source&reverse  Sorting by 'source' with reverse


    return render_template('index.html', news=news_page)