from flask import Blueprint
from flask import render_template
from app.services.visitas import registrar_visita,contar_visitas


home_bp = Blueprint(
    "home",
    __name__
)

@home_bp.route("/")
def home():
    registrar_visita()

    cantidad = contar_visitas()
    
    return render_template(
        "home.html",
        visitas=cantidad
    )

