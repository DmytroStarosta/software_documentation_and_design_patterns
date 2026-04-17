from flask import Flask, Blueprint, render_template, request, redirect, url_for
from app.bll.app_bll.interface_app_bll import IAppBll
from app import db
from app.bll.app_bll import app_bll
from app.models import User

bp = Blueprint('devices', __name__, template_folder='../templates')

@bp.route('/')
def index():
    devices = app_bll.get_all_devices()
    return render_template('index.html', devices=devices)

# Сторінка з формою додавання
@bp.route('/add', methods=['GET'])
def add_device_page():
    return render_template('add_device.html')

# Обробка даних форми
@bp.route('/add', methods=['POST'])
def add_device():
    user = db.session.query(User).first()
    if not user:
        return "Error: No users found in database.", 400

    app_bll.add_device(
        request.form.get('name'),
        request.form.get('mac_address'),
        request.form.get('location'),
        user.id
    )
    return redirect(url_for('devices.index'))

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_device(id):
    if request.method == 'POST':
        app_bll.update_device(
            id,
            request.form.get('name'),
            request.form.get('mac_address'),
            request.form.get('location')
        )
        return redirect(url_for('devices.index'))

    device = app_bll.get_device_by_id(id)
    return render_template('edit.html', device=device)

@bp.route('/delete/<int:id>')
def delete_device(id):
    app_bll.delete_device(id)
    return redirect(url_for('devices.index'))

class AppPresentation:
    def __init__(self, bll: IAppBll):
        self.bll = bll
        self.session = db.session

    def create_db(self, app: Flask):
        self.bll.create_db(app)
        self.session.commit()
        return True