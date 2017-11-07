from models.topic import Topic
from models.node import Node
from routes import *


main = Blueprint('topic', __name__)

Model = Topic


# @main.route('/')
# def index():
#     ms = Model.query.all()
#     return render_template('topic_index.html', node_list=ms)


@main.route('/new')
@login_required
def new():
    u = current_user()
    return render_template('topic_new.html', user=u)


@main.route('/<int:id>')
def show(id):
    u = current_user()
    m = Model.query.get(id)
    # 拿到当前 node
    node = Node.query.get(m.node_id)
    # 拿到所有 node
    nodes = Node.query.all()
    return render_template('topic.html', topic=m, user=u, node=node, node_list=nodes)


# @main.route('/edit/<id>')
# def edit(id):
#     t = Model.query.get(id)
#     return render_template('topic_edit.html', todo=t)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    u = current_user()
    m.user = u
    m.username = u.username
    valid, msgs = m.valid_post()
    if valid:
        m.save()
        return redirect(url_for('node.show', id=m.node_id))
    else:
        return render_template('topic_new.html', user=u, msgs=msgs[0])


@main.route('/delete/<int:id>')
def delete(id):
    m = Model.query.get(id)
    user_id = m.user_id
    m.delete()
    return redirect(url_for('user.index', id=user_id))


# @main.route('/update/<int:id>', methods=['POST'])
# def update(id):
#     form = request.form
#     t = Model.query.get(id)
#     t.update(form)
#     return redirect(url_for('.index'))