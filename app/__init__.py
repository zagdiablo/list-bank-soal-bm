from flask import Flask
from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()
DB_NAME = "app.db"


def jalankan_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
