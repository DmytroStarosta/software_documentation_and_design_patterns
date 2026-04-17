import csv
from flask import Flask
from sqlalchemy_utils import database_exists, create_database

from app.dal.app_dal.interface_app_dal import IAppDal
from app import db
from app.models import User, Device


class AppDal(IAppDal):
    def read_csv(self):
        data_dict = {}
        current_table = None
        with open("data.csv", newline="", encoding="utf-8") as csvfile:
            for line in csvfile:
                line = line.strip()
                if not line: continue
                if line.startswith("#"):
                    current_table = line[1:]
                    data_dict[current_table] = []
                else:
                    data_dict[current_table].append(line)
            return data_dict

    def create_table(self, app: Flask):
        # ВИДАЛИЛИ db.init_app(app), щоб не було RuntimeError
        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])

        with app.app_context():
            # Створюємо таблиці (тільки User та Device)
            db.create_all()

    def write_table(self, data: dict):
        user_map = {}
        # User
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

        # Device
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

        db.session.commit()

    # --- CRUD Методи ---
    def get_all_devices(self):
        return db.session.query(Device).all()

    def get_device_by_id(self, device_id: int):
        return db.session.query(Device).get(device_id)

    def add_device(self, name: str, mac_address: str, location: str, user_id: int):
        new_device = Device(name=name, mac_address=mac_address, location=location, user_id=user_id)
        db.session.add(new_device)
        db.session.commit()

    def update_device(self, device_id: int, name: str, mac_address: str, location: str):
        device = db.session.query(Device).get(device_id)
        if device:
            device.name = name
            device.mac_address = mac_address
            device.location = location
            db.session.commit()

    def delete_device(self, device_id: int):
        device = db.session.query(Device).get(device_id)
        if device:
            db.session.delete(device)
            db.session.commit()