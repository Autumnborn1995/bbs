import json
from routes import *

main = Blueprint('dva', __name__)


def save(n):
    n = str(n)
    with open('static/count.txt', 'w', encoding='utf-8') as f:
        f.write(n)


def load():
    with open('static/count.txt', 'r', encoding='utf-8') as f:
        n = f.read()
        return int(n)


@main.route('/')
def index():
    c = load()
    return render_template('dva.html', count=c)


@main.route('/add')
def add():
    c = load()
    c += 1
    save(c)
    r = {
        'success': True,
        'count': c,
    }
    return json.dumps(r, ensure_ascii=False)