from flask import Flask
from sqlalchemy_utils import database_exists, create_database

from app.dal.app_dal.interface_app_dal import IAppDal
from app import db
from app.models import *

class AppDal(IAppDal):
    def read_csv(self):
        data_dict = {}
        current_table = None
        with open("data.csv", newline="", encoding="utf-8") as csvfile:
            for  line in csvfile:
                line = line.strip()
                if not line:
                    continue
                if line.startswith("#"):
                    current_table = line[1:]
                    data_dict[current_table] = []
                else:
                    data_dict[current_table].append(line)
            return data_dict


    def create_table(self, app: Flask):
        db.init_app(app)

        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])


        with app.app_context():
            db.create_all()

    def write_table(self, data: dict):
        pass