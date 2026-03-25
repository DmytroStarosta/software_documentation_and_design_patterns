from abc import ABC, abstractmethod

class IAppBll(ABC):
    @abstractmethod
    def create_db(self):
        pass
