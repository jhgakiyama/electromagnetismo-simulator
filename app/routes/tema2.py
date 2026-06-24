from flask import render_template
from flask import Blueprint
from app.plots.tema2_plot import visualizacion_conceptual_2a

bp = Blueprint(
    "tema2",
    __name__
)

@bp.route("/tema2/demo")
def tema2_demo():

    fig = visualizacion_conceptual_2a()

    return render_template(
        "tema2_demo.html",
        grafico=fig.to_html(
            full_html=False
        )
    )