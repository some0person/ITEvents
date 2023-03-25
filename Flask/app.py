from flask import Flask, render_template, request


from database.database import News
app = Flask(__name__)


# @app.route('/', methods=['GET'], defaults={'uid': 'zero'})
@app.route('/', methods=['GET'])
def home():
    args = request.args
    sorting_arg, reverse_arg, per_page_arg, page_arg, filterby_arg, filterword_arg = \
        args.get('sort', default='id'), 'reverse' in args, args.get('perpage', default='8'), \
        args.get('p', default='0'), args.get('filterby', default='title'), args.get('filterword', default='')
    page, per_page = int(page_arg) if page_arg.isdecimal() else 0, int(per_page_arg) if per_page_arg.isdecimal() and int(per_page_arg) >= 1 else 10

    news_page = News().getNews(page * per_page, (page + 1) * per_page, sorting_arg, reverse_arg, filterby_arg, filterword_arg)
        
    # Pages usage examples:
    #   http://127.0.0.1:5000/?p=0&perpage=15   Page 0 with 15 articles on each
    #   http://127.0.0.1:5000/?p=5&perpage=2    Page 5 with 2 articles on each

    # Sorting examples:
    #   http://127.0.0.1:5000/?sort=source  Sorting by 'source'
    #   http://127.0.0.1:5000/?sort=source&reverse  Sorting by 'source' with reverse

    return render_template('index.html', news=news_page)
