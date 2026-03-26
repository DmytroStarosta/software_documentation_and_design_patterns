from app import db

class Camera(db.Model):
    __tablename__ = 'camera'
    id = db.Column(db.Integer, primary_key=True)
    image_quality = db.Column(db.String(120), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)

    @staticmethod
    def get_columns() -> str:
        return '#camera\nid,image_quality,device_id\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i},{i}px,{i}\n'