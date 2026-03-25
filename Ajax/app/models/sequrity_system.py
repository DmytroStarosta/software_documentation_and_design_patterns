from app import db

class SequritySystem(db.Model):
    __tablename__ = 'sequrity_system'
    id = db.Column(db.Integer, primary_key=True)
    access_code = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)