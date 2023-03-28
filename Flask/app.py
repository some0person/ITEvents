from flask import Flask, render_template, request


from database.database import News
app = Flask(__name__)


def rmparam(query_string, *params_to_remove):
    params = [param.split('=') for param in query_string.split('&')]
    return '&'.join(['='.join(param) for param in params if param[0] not in params_to_remove])


@app.route('/', methods=['GET'])
def home():
    args = request.args
    sorting_arg, reverse_arg, per_page_arg, page_arg, filterby_arg, filterword_arg = \
        args.get('sort', default='id'), 'r' in args or args.get('r') != '0', args.get('perpage', default='8'), \
        args.get('p', default='0'), args.get('filterby', default='title'), args.get('filterword', default='')
    
    per_page = int(per_page_arg) if per_page_arg.isdecimal() and int(per_page_arg) >= 1 else 10
    query_string = request.query_string.decode("utf-8")

    # Should be replaced later with database functions
    posts_amount = 800
    pages_amount = int(posts_amount / per_page + 0.9)

    page = int(page_arg) if page_arg.isdecimal() and 1 <= int(page_arg) <= pages_amount \
        else 1 if int(page_arg) <= pages_amount else pages_amount

    news_page = News().getNews((page - 1) * per_page, page * per_page, sorting_arg, reverse_arg, filterby_arg, filterword_arg)

    pages_buttons = \
        [i + (page - 4 if 4 < page <= pages_amount - 4 else 0 if page < pages_amount - 4 else pages_amount - 7) \
         for i in range(1, min(7, pages_amount) + 1)]    
        
    # Pages usage examples:
    #   http://127.0.0.1:5000/?p=0&perpage=15   Page 0 with 15 articles on each
    #   http://127.0.0.1:5000/?p=5&perpage=2    Page 5 with 2 articles on each

    # Sorting examples:
    #   http://127.0.0.1:5000/?sort=source  Sorting by 'source'
    #   http://127.0.0.1:5000/?sort=source&r=1  Sorting by 'source' with reverse

    return render_template('index.html', news=news_page, pages_buttons=pages_buttons, pages_amount=pages_amount,\
                           page=page, pagestr=str(page), qs=query_string, rmparam=rmparam)
