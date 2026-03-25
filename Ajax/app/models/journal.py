from app import db

class Journal(db.Model):
    __tablename__ = 'journal'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
