from abc import ABC, abstractmethod

from flask import Flask


class IAppBll(ABC):
    @abstractmethod
    def create_db(self, app: Flask):
        pass
