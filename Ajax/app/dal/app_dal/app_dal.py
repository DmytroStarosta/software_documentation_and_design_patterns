import csv
from flask import Flask
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime

from app.dal.app_dal.interface_app_dal import IAppDal
from app import db
from app.models import *

class AppDal(IAppDal):
    def read_csv(self):
        data_dict = {}
        current_table = None
        with open("data.csv", newline="", encoding="utf-8") as csvfile:
            for  line in csvfile:
                line = line.strip()
                if not line:
                    continue
                if line.startswith("#"):
                    current_table = line[1:]
                    data_dict[current_table] = []
                else:
                    data_dict[current_table].append(line)
            return data_dict


    def create_table(self, app: Flask):
        db.init_app(app)

        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])


        with app.app_context():
            db.create_all()

    def write_table(self, data: dict):
        user_map = {}
        device_map = {}

        # user
        reader = csv.DictReader(data["user"])
        for row in reader:
            user = User(
                fullname=row["fullname"],
                email=row["email"],
                phone_number=row["phone_number"],
            )
            db.session.add(user)
            db.session.flush()
            user_map[row["id"]] = user.id

        #device
        reader = csv.DictReader(data["device"])
        for row in reader:
            device = Device(
                name=row["name"],
                mac_address=row["mac_address"],
                location=row["location"],
                user_id=int(user_map[row["user_id"]]),
            )
            db.session.add(device)
            db.session.flush()
            device_map[row["id"]] = device.id

        #sensor
        reader = csv.DictReader(data["sensor"])
        for row in reader:
            sensor = Sensor(
                data_type=row["data_type"],
                device_id=int(device_map[row["device_id"]]),
            )
            db.session.add(sensor)
            db.session.flush()

        #camera
        reader = csv.DictReader(data["camera"])
        for row in reader:
            camera = Camera(
                image_quality=row["image_quality"],
                device_id=int(device_map[row["device_id"]]),
            )
            db.session.add(camera)
            db.session.flush()

        #alarm_message
        reader = csv.DictReader(data["alarm_message"])
        for row in reader:
            alarm_message = AlarmMessage(
                number=row["number"],
                timestamp=datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S'),
                status=row["status"],
                device_id=int(device_map[row["device_id"]]),
            )
            db.session.add(alarm_message)
            db.session.flush()

        #journal
        reader = csv.DictReader(data["journal"])
        for row in reader:
            journal = Journal(
                name=row["name"],
            )
            db.session.add(journal)
            db.session.flush()

        #security_system
        reader = csv.DictReader(data["security_system"])
        for row in reader:
            security_system = SecuritySystem(
                access_code=row["access_code"],
                status=row["status"],
                location=row["location"],
            )
            db.session.add(security_system)
            db.session.flush()



