from app.models import *


def create_csv():
    tables: list = [AlarmMessage, Camera, Device, Journal, Sensor, SecuritySystem, User]

    with open('data.csv', 'w', encoding='utf-8') as file:
        for table in tables:
            table_record = table.get_columns()
            file.write(table_record)
            for i in range(150):
                record = table.get_string(i+1)
                file.write(record)

if __name__ == '__main__':
    print("Creating csv📝 'data.csv'")
    print('...')
    create_csv()
    print("Created csv📋 'data.csv'")