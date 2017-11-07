from . import ModelMixin
from . import db
from . import created_time


class Comment(db.Model, ModelMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.Integer)
    username = db.Column(db.String())
    # has relationship with comments
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = created_time()

    def json(self):
        d = dict(
            id=self.id,
            content=self.content,
            username=self.username,
            created_time=self.created_time,
            user_id=self.user_id,
            topic_id=self.topic_id,
        )
        return d
