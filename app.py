from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db

import os

app = Flask(__name__)
manager = Manager(app)


def register_routes(app):
    from routes.auth import main as routes_auth
    from routes.node import main as routes_node
    from routes.topic import main as routes_topic
    from routes.user import main as routes_user
    from routes.comment import main as routes_comment
    from routes.dva import main as routes_dva

    app.register_blueprint(routes_auth)
    app.register_blueprint(routes_node, url_prefix='/node')
    app.register_blueprint(routes_topic, url_prefix='/topic')
    app.register_blueprint(routes_user, url_prefix='/user')
    app.register_blueprint(routes_comment, url_prefix='/comment')
    app.register_blueprint(routes_dva, url_prefix='/dva')


db_config = {
    'DRIVER': 'pymysql',
    'USER': 'root',
    'PASSWORD': 'root',
    'HOST': '127.0.0.1',
    'PORT': 3306,
    'NAME': 'bbs'
}

db_path = 'bbs.sqlite'


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pwd@localhost/bbs'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(**db_config)
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    print('server run')
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=80,
    )
    app.run(**config)


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configured_app()
    manager.run()
