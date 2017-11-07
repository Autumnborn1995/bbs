from models.comment import Comment
from routes import *

main = Blueprint('comment', __name__)

Model = Comment


@main.route('/add', methods=['POST'])
@login_required
def add():
    form = request.form
    m = Model(form)
    m.topic_id = int(form.get('topic_id'))
    # 惨，username 和 user_id 都要手动添加
    u = current_user()
    m.username = u.username
    m.user_id = u.id
    m.save()
    return redirect(url_for('topic.show', id=m.topic_id))


@main.route('/delete/<int:id>')
def delete(id):
    c = Model.query.get(id)
    c.delete()
    return redirect(url_for('topic.show', id=c.topic_id))


# @main.route('/')
# def index():
#     ms = Model.query.all()
#     return render_template('topic_index.html', node_list=ms)


# @main.route('/new')
# def new():
#     return render_template('topic_new.html')


# @main.route('/<int:id>')
# def show(id):
#     m = Model.query.get(id)
#     return render_template('topic.html', topic=m)


# @main.route('/edit/<id>')
# def edit(id):
#     t = Model.query.get(id)
#     return render_template('topic_edit.html', todo=t)


# @main.route('/update/<int:id>', methods=['POST'])
# def update(id):
#     form = request.form
#     t = Model.query.get(id)
#     t.update(form)
#     return redirect(url_for('.index'))
