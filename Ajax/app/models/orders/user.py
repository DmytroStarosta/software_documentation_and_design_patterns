from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(120), nullable=False)

    @staticmethod
    def get_columns() -> str:
        return '#user\nid,fullname,email,phone_number\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i},User{i},email@lpnu.ua{i},phone_number{i}\n'
