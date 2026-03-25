from app.bll.app_bll.interface_app_bll import IAppBll
from app import db


class AppPresentation:
    def __init__(self, bll: IAppBll):
        self.bll = bll
        self.session = db.session()


    def create_db(self):
        try:
            self.bll.create_db()
            self.session.commit()
            return True
        except:
            self.session.rollback()
            return False