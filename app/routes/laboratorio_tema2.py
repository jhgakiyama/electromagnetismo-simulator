from flask import Blueprint
from flask import render_template
from flask import request


from app.physics.laboratorio import calcular_simulacion


bp = Blueprint(
    "tema2_laboratorio",
    __name__
)

@bp.route("/tema2/laboratorio", methods=["GET", "POST"])
def tema2_laboratorio():
    template = "tema2_laboratorio.html"
    
    if request.method == "POST":
        corriente1 = float(request.form["corriente1"])
        corriente2 = float(request.form["corriente2"])
        sentido1 = request.form["sentido1"]
        sentido2 = request.form["sentido2"]
        px = float(request.form["px"])
        py = float(request.form["py"])
    else:
        corriente1=1.0,
        sentido1="entrante",
        corriente2=1.0,
        sentido2="entrante",
        px=1.0,
        py=1.0
    
    resultado = calcular_simulacion(
        corriente1=1,
        sentido1="entrante",
        corriente2=1,
        sentido2="entrante",
        px=1,
        py=1
    )
    
    
    return render_template(
        template,
        resultado=resultado,
        grafico=resultado["grafico"].to_html(
            full_html=False,
            include_plotlyjs="cdn"
        )
    )