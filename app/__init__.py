from flask import Flask

from app.routes.conductor import conductor_bp
from app.routes.home import home_bp
from app.routes.tema2 import bp as tema2_bp


def create_app():

    app = Flask(__name__)

    app.register_blueprint(conductor_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(tema2_bp)
    return app