from flask import Flask

from app.routes.conductor import conductor_bp
from app.routes.home import home_bp
from app.routes.tema2 import bp as tema2_bp
from app.routes.laboratorio_tema2 import bp as labo_tema2
from app.routes.health import health_bp
from app.errors import register_error_handlers


def create_app():

    app = Flask(__name__)

    app.register_blueprint(conductor_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(tema2_bp)
    app.register_blueprint(labo_tema2)
    app.register_blueprint(health_bp)

    register_error_handlers(app)
    
    return app