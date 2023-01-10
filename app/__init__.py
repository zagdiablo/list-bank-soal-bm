from flask import Flask
from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()
DB_NAME = "app.db"


def jalankan_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True

    return app
