from flask import Blueprint
from flask import render_template
from app.services.visitas import registrar_visita


home_bp = Blueprint(
    "home",
    __name__
)

@home_bp.route("/")
def home():
    registrar_visita()
    
    return render_template("home.html")

