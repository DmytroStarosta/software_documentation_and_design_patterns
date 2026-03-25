from abc import ABC, abstractmethod

class IAppDal(ABC):
    @abstractmethod
    def read_csv(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def write_table(self):
        pass
