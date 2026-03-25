from flask import Flask
from sqlalchemy_utils import database_exists, create_database

from app.dal.app_dal.interface_app_dal import IAppDal
from app import db
from app.models import *
from app.core.config import DATABASE_URI

class AppDal(IAppDal):
    def read_csv(self):
        pass

    def create_table(self, app: Flask):
        db.init_app(app)

        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])


        with app.app_context():
            db.create_all()

    def write_table(self, data: dict):
        pass