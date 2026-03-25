import datetime

from app import db

class AlarmMessage(db.Model):
    __tablename__ = 'alarm_message'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    status = db.Column(db.String(120), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)
