from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config.Database import FULL_URL_DB


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app=Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.debug = True

    db.init_app(app)
    return app