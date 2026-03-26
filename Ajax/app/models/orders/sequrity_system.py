from app import db

class SecuritySystem(db.Model):
    __tablename__ = 'security_system'
    id = db.Column(db.Integer, primary_key=True)
    access_code = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)