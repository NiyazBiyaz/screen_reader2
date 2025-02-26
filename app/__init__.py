import flask
from .routes import main


def create_app():
    app = flask.Flask(__name__)

    app.register_blueprint(main)

    return app
