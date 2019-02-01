from flask import Flask
from app.web import web
from app.models.base import db, migrate
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'web.login'
login_manager.login_message = '请先登录或注册'

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    app.register_blueprint(web)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    return app