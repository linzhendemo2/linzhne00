from flask import Blueprint

from App.models import db

blue = Blueprint('blue', __name__)

@blue.route('/')
def hello():
    return 'hello linzhen'

@blue.route('/data/')
def data():
    user = db.create_all()
    return 'sucess'