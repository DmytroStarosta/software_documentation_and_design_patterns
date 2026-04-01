from app import db

class Journal(db.Model):
    __tablename__ = 'journal'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    @staticmethod
    def get_columns() -> str:
        return '#journal\nid,name\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i},name{i}\n'