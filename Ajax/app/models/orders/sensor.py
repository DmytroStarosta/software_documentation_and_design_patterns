from app import db

class Sensor(db.Model):
    __tablename__ = 'sensor'
    id = db.Column(db.Integer, primary_key=True)
    data_type = db.Column(db.String(120), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)

    @staticmethod
    def get_columns() -> str:
        return '#sensor\nid,data_type,device_id\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i},type{i},{i}\n'