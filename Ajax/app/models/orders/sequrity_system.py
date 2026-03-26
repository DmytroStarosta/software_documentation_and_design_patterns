from app import db

class SecuritySystem(db.Model):
    __tablename__ = 'security_system'
    id = db.Column(db.Integer, primary_key=True)
    access_code = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)

    @staticmethod
    def get_columns() -> str:
        return '#security_system\nid,access_code,status,location\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i},code:{i},secure{i},Bandery St.{i}\n'