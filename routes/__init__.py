from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for
from flask import abort

from models.user import User
from functools import wraps

import time


def log(*args, **kwargs):
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()) + 28800)
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


def current_user():
    uid = session.get('uid')
    if uid is not None:
        u = User.query.get(uid)
    else:
        u = '游客'
    return u


def admin_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        print('admin required')
        u = current_user()
        if u.id != 1:
            print('not admin')
            abort(404)
        return f(*args, **kwargs)

    return function


def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        u = current_user()
        if u == '游客' or u == None:
            return redirect('/signin')
        return f(*args, **kwargs)

    return function
