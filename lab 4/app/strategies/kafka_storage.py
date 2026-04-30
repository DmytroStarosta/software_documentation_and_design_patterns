import json
from kafka import KafkaProducer
from app.strategies.base import StorageStrategy

class KafkaStrategy(StorageStrategy):
    def __init__(self, bootstrap_servers, topic):
        self.producer = KafkaProducer(
            bootstrap_servers=[bootstrap_servers],
            api_version=(0, 11, 5),
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.topic = topic

    def save(self, data: dict):
        self.producer.send(self.topic, value=data)
        self.producer.flush()
        print(f" Sent to Kafka (topic: {self.topic})")