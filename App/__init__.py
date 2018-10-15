

from flask import Flask

from App.apis import blue


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=blue)
    return app



