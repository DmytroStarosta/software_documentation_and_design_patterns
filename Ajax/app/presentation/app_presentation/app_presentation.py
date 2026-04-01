from flask import Flask

from app.bll.app_bll.interface_app_bll import IAppBll
from app import db


class AppPresentation:
    def __init__(self, bll: IAppBll):
        self.bll = bll
        self.session = db.session


    def create_db(self, app: Flask):
        # try:
        #     self.bll.create_db(app)
        #     self.session.commit()
        #     return True
        # except Exception as e:
        #     self.session.rollback()
        #     print(e)
        #     return False
        self.bll.create_db(app)
        self.session.commit()
        return True