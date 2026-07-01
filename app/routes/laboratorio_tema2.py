from flask import render_template
from flask import Blueprint
from app.plots.tema2_plot import visualizacion_resultado_final


bp = Blueprint(
    "tema2_laboratorio",
    __name__
)

@bp.route("/tema2/laboratorio")
def tema2_laboratorio():

    grafico = visualizacion_resultado_final()
    template = "tema2_laboratorio.html"
    
    return render_template(
        template,
        grafico=grafico.to_html(
            full_html=False,
            include_plotlyjs="cdn"
        )
    )