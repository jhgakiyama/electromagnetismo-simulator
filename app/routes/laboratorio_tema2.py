from flask import render_template
from flask import Blueprint
# from app.plots.tema2_plot import visualizacion_resultado_final
from app.physics.laboratorio import calcular_simulacion


bp = Blueprint(
    "tema2_laboratorio",
    __name__
)

@bp.route("/tema2/laboratorio")
def tema2_laboratorio():

    # grafico = visualizacion_resultado_final()
    resultado = calcular_simulacion(
        corriente1=1,
        sentido1="entrante",
        corriente2=1,
        sentido2="entrante",
        px=1,
        py=1
    )
    template = "tema2_laboratorio.html"
    
    return render_template(
        template,
        resultado=resultado,
        grafico=resultado["grafico"].to_html(
            full_html=False,
            include_plotlyjs="cdn"
        )
    )