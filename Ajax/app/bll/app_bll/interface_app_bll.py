from abc import ABC, abstractmethod
from flask import Flask

class IAppBll(ABC):
    @abstractmethod
    def create_db(self, app: Flask):
        pass

    @abstractmethod
    def get_all_devices(self):
        pass

    @abstractmethod
    def get_device_by_id(self, device_id: int):
        pass

    @abstractmethod
    def add_device(self, name: str, mac_address: str, location: str, user_id: int):
        pass

    @abstractmethod
    def update_device(self, device_id: int, name: str, mac_address: str, location: str):
        pass

    @abstractmethod
    def delete_device(self, device_id: int):
        pass