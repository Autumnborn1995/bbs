from models.node import Node
from models.topic import Topic
from models.user import User
from routes import *

main = Blueprint('node', __name__)

Model = Node


@main.route('/')
def index():
    u = current_user()
    n = Model.query.all()
    m = Model.query.get(1)
    topics = Topic.query.filter_by(node_id=1).all()
    topics.reverse()
    return render_template('node.html', user=u, node_list=n, node=m, topics=topics)


@main.route('/<int:id>')
def show(id):
    u = current_user()
    n = Model.query.all()
    m = Model.query.get(id)
    topics = Topic.query.filter_by(node_id=m.id).all()
    topics.reverse()
    return render_template('node.html', user=u, node_list=n, node=m, topics=topics)


@main.route('/admin')
@admin_required
def admin():
    u = current_user()
    all_user = User.query.all()
    ms = Model.query.all()
    return render_template('node_admin.html', user=u, node_list=ms, all_user=all_user)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('.admin'))


@main.route('/delete/<int:id>')
def delete(id):
    m = Model.query.get(id)
    m.delete()
    return redirect(url_for('.new'))


    # @main.route('/edit/<id>')
    # def edit(id):
    #     t = Model.query.get(id)
    #     return render_template('node_edit.html', todo=t)


    # @main.route('/update/<int:id>', methods=['POST'])
    # def update(id):
    #     form = request.form
    #     t = Model.query.get(id)
    #     t.update(form)
    #     return redirect(url_for('.index'))
