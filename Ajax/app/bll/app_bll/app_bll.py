from flask import Flask

from app.bll.app_bll.interface_app_bll import IAppBll
from app.dal.app_dal.interface_app_dal import IAppDal


class AppBll(IAppBll):
    def __init__(self, dal: IAppDal):
        self.dal = dal

    def create_db(self, app: Flask):
        data_dict = self.dal.read_csv()
        self.dal.create_table(app)
        self.dal.write_table(data_dict)
