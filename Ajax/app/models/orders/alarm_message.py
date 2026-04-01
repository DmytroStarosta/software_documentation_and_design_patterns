import datetime

from app import db

class AlarmMessage(db.Model):
    __tablename__ = 'alarm_message'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    status = db.Column(db.String(120), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)

    @staticmethod
    def get_columns() -> str:
        return '#alarm_message\nid,number,timestamp,status,device_id\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i},{i},2025-11-11 11:11:11,status{i},{i}\n'