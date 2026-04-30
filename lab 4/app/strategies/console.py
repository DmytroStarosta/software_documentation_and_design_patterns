from app.strategies.base import StorageStrategy

class ConsoleStrategy(StorageStrategy):
    def save(self, data: dict):
        print(f"[CONSOLE LOG]: {data}")