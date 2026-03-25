from abc import ABC, abstractmethod

from flask import Flask


class IAppDal(ABC):
    @abstractmethod
    def read_csv(self):
        pass

    @abstractmethod
    def create_table(self, app: Flask):
        pass

    @abstractmethod
    def write_table(self, data: dict):
        pass
