import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models import User, Device


def create_csv():
    tables: list = [User, Device]

    with open('data.csv', 'w', encoding='utf-8') as file:
        for table in tables:
            file.write(f"#{table.__tablename__}\n")

            columns = table.get_columns()
            file.write(columns)

            for i in range(5):
                record = table.get_string(i + 1)
                file.write(record)


if __name__ == '__main__':
    print("Creating csv📝 'data.csv'...")
    try:
        create_csv()
        print("Created csv📋 'data.csv' ✅")
    except Exception as e:
        print(f"Error: {e}")