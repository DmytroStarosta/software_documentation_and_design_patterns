from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.core.config import DATABASE_URI

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='presentation/templates')
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)

    from app.presentation.app_presentation.app_presentation import bp
    app.register_blueprint(bp)

    return app