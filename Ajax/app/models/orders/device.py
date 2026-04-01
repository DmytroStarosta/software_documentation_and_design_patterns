from app import db

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    mac_address = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @staticmethod
    def get_columns() -> str:
        return '#device\nid,name,mac_address,location,user_id\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i},device{i},MAC{i},Franka St.{i},{i}\n'
