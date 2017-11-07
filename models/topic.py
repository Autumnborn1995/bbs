from . import ModelMixin
from . import db
from . import created_time


class Topic(db.Model, ModelMixin):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    username = db.Column(db.String())
    created_time = db.Column(db.Integer)
    # has relationship with comments
    comments = db.relationship('Comment', backref="topic")

    node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.node_id = form.get('node_id', 0)
        self.created_time = created_time()

    # 验证要发表帖子的合法性
    def valid_post(self):
        valid_title_len = len(self.title) >= 1
        valid_content_len = len(self.content) >= 10
        msgs = []
        if not valid_title_len:
            message = '标题不能为空！'
            msgs.append(message)
        elif not valid_content_len:
            message = '内容长度必须大于 10 ！'
            msgs.append(message)
        status = valid_title_len and valid_content_len
        return status, msgs
