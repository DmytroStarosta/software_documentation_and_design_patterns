from app import db

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    mac_address = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
