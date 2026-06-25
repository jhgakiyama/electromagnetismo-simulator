from flask import render_template
from flask import Blueprint
from app.plots.tema2_plot import visualizacion_conceptual_2a, visualizacion_conceptual_2b

bp = Blueprint(
    "tema2",
    __name__
)

@bp.route("/tema2/demo")
def tema2_demo():

    # fig = visualizacion_conceptual_2a()
    fig = visualizacion_conceptual_2b()

    return render_template(
        "tema2_demo.html",
        grafico=fig.to_html(
            full_html=False
        )
    )