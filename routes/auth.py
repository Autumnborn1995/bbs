from models.user import User
from models.node import Node
from models.topic import Topic
from routes import *

main = Blueprint('auth', __name__)

Model = User


@main.route('/')
def index():
    u = current_user()
    n = Node.query.all()
    m = Node.query.get(1)
    topics = Topic.query.filter_by(node_id=1).all()
    topics.reverse()
    return render_template('node.html', user=u, node_list=n, node=m, topics=topics)


@main.route('/signin')
def signin():
    return render_template('signin.html', msgs='')


@main.route('/signup')
def signup():
    return render_template('signup.html', msgs='')


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u = User(form)
    user = Model.query.filter_by(username=u.username).first()
    valid, msgs = u.valid_login(user)
    if valid:
        session.permanent = True
        session['uid'] = user.id
        return redirect(url_for('.index'))
    else:
        return render_template('signin.html', msgs=msgs[0])


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    valid, msgs = u.valid_register()
    if valid:
        u.save()
        return redirect(url_for('.signin'))
    else:
        return render_template('signup.html', msgs=msgs[0])


@main.route('/signout')
def logout():
    session.permanent = False
    session['uid'] = None
    return redirect(url_for('.index'))