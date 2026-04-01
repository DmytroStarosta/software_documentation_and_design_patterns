from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.core.config import DATABASE_URI

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    return app

