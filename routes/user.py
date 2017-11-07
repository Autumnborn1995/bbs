from models.topic import Topic
from models.user import User
from routes import *


main = Blueprint('user', __name__)

Model = User


@main.route('/<int:id>')
def index(id):
    m = Model.query.get(id)
    u = current_user()
    topics = Topic.query.filter_by(user_id=m.id).all()
    n = len(topics)
    topics.reverse()
    return render_template('user_index.html', user=u, other=m, topics=topics, topic_num=n)


# @main.route('/new/<int:id>')
# def new(id):
#     u = current_user()
#     return render_template('topic_new.html', node_id=id, user=u)


# @main.route('/<int:id>')
# def show(id):
#     u = current_user()
#     m = Model.query.get(id)
#     return render_template('topic.html', topic=m, user=u)


# @main.route('/edit/<id>')
# def edit(id):
#     t = Model.query.get(id)
#     return render_template('topic_edit.html', todo=t)


# @main.route('/add/<int:id>', methods=['POST'])
# def add(id):
#     form = request.form
#     m = Model(form)
#     m.node_id = id
#     u = current_user()
#     m.user = u
#     m.username = u.username
#     m.save()
#     return redirect(url_for('node.show', id=id))


# @main.route('/delete/<int:id>')
# def delete(id):
#     m = Model.query.get(id)
#     m.delete()
#     return redirect(url_for('node.show', id=m.node_id))


# @main.route('/update/<int:id>', methods=['POST'])
# def update(id):
#     form = request.form
#     t = Model.query.get(id)
#     t.update(form)
#     return redirect(url_for('.index'))