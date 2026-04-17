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

    def get_all_devices(self):
        return self.dal.get_all_devices()

    def get_device_by_id(self, device_id: int):
        return self.dal.get_device_by_id(device_id)

    def add_device(self, name: str, mac_address: str, location: str, user_id: int):
        self.dal.add_device(name, mac_address, location, user_id)

    def update_device(self, device_id: int, name: str, mac_address: str, location: str):
        self.dal.update_device(device_id, name, mac_address, location)

    def delete_device(self, device_id: int):
        self.dal.delete_device(device_id)