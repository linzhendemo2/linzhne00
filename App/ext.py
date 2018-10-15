from flask_migrate import Migrate

from App.apis import blue
from App.models import db


migrate = Migrate()

def init_ext(app):
    app.register_blueprint(blueprint=blue)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/linzhen'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)
