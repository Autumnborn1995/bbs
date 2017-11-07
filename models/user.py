import hashlib
import os

from . import ModelMixin
from . import db


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    comments = db.relationship('Comment', backref='user', foreign_keys='Comment.user_id')
    topics = db.relationship('Topic', backref='user', foreign_keys='Topic.user_id')

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.captcha = form.get('captcha', '')

    def valid_login(self, user):
        msgs = ['帐号或密码错误']
        if user is not None:
            username_equals = user.username == self.username
            password_equals = user.password == self.password
            # 返回 'bool' object is not iterable
            # 问题出在这里，如果登录成功这里就只有
            msgs.append('')
            return username_equals and password_equals, msgs
        else:
            return False, msgs

    # 验证注册用户的合法性的
    def valid_register(self):
        valid_username = User.query.filter_by(username=self.username).first() == None
        valid_username_len = len(self.username) >= 3
        valid_password_len = len(self.password) >= 3
        valid_captcha = self.captcha == '1988'
        msgs = []
        if not valid_username:
            message = '用户名已经存在'
            msgs.append(message)
        elif not valid_username_len:
            message = '用户名长度必须大于等于 3'
            msgs.append(message)
        elif not valid_password_len:
            message = '密码长度必须大于等于 3'
            msgs.append(message)
        elif not valid_captcha:
            message = '邀请码错误'
            msgs.append(message)
        # elif not valid_captcha:
        #     message = '验证码必须输入 3'
        #     msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len and valid_captcha
        return status, msgs