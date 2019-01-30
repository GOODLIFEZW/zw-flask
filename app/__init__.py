from flask import Flask
from app.web import web
from app.models.base import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    app.register_blueprint(web)
    db.init_app(app)
    migrate.init_app(app, db)
    return app