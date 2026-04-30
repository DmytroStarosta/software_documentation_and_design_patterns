import redis
import json
from app.strategies.base import StorageStrategy

class RedisStrategy(StorageStrategy):
    def __init__(self, host, port):
        self.client = redis.Redis(host=host, port=port)
        self.key = "taxi_trips_list"

    def save(self, data: dict):
        self.client.rpush(self.key, json.dumps(data))

        print(f" Saved to Redis: {data}")