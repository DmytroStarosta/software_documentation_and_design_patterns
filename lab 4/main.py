import pandas as pd
import json
from app.strategies import ConsoleStrategy, RedisStrategy, KafkaStrategy


class DataProcessor:
    def __init__(self, strategy):
        self._strategy = strategy

    def run(self, file_path):
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            self._strategy.save(row.to_dict())


def get_strategy():
    with open('config.json', 'r') as f:
        config = json.load(f)

    s_type = config['storage_type']
    if s_type == "redis":
        return RedisStrategy(**config['redis_config'])
    elif s_type == "kafka":
        return KafkaStrategy(**config['kafka_config'])
    return ConsoleStrategy()


if __name__ == "__main__":
    strategy = get_strategy()
    processor = DataProcessor(strategy)
    processor.run('dataset.csv')