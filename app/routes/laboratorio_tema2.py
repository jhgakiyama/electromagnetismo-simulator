from flask import Blueprint
from flask import render_template
from flask import request
from app.physics.laboratorio import calcular_simulacion
from app.plots.laboratorio_plot import visualizacion_resultado_laboratorio


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
        corriente1=1.0
        sentido1="entrante"
        corriente2=1.0
        sentido2="entrante"
        px=1.0
        py=1.0
    
    resultado = calcular_simulacion(
        corriente1=corriente1,
        sentido1=sentido1,
        corriente2=corriente2,
        sentido2=sentido2,
        px=px,
        py=py
    )
    # print(resultado["parametros"])
    
    grafico = visualizacion_resultado_laboratorio(resultado)

    return render_template(
        template,
        resultado=resultado,
        grafico=grafico.to_html(
            full_html=False,
            include_plotlyjs="cdn"
        )
    )