from flask import render_template
from flask import Blueprint
from app.plots.tema2_plot_vista_concep1 import visualizacion_conceptual_2a
from app.plots.tema2_plot_vista_concep2 import visualizacion_conceptual_2b
from app.plots.tema2_plot import (
    visualizacion_ejercicio_2,
    visualizacion_resolucion_p1,
    visualizacion_resolucion_i2
    )
from app.physics.tema2 import calcular_radio, magnitud_campo, componentes_campo, magnitud_vector


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

@bp.route("/tema2/ejercicio")
def ejercicio():
    fig = visualizacion_ejercicio_2()

    return render_template(
        "tema2_ejercicio.html",
        grafico=fig.to_html(
            full_html=False,
            include_plotlyjs="cdn"
        )
    )

@bp.route("/tema2/resolucion/p1")
def resolucion_p1():
    # Todos los calculos son para P1
    
    # Valores del ejericio
    i1 = (0, 0)
    i2 = (2, 0)
    p1 = (1, 1)
    corriente1 = 1
    corriente2 = 1

    # Valores para B1  
    dx1, dy1, r1 = calcular_radio(i1, p1)
    b1 = magnitud_campo(corriente1, r1)
    bx1, by1 = componentes_campo(corriente1,r1,dx1,dy1,"entrante")
    
    # Valores para B2
    dx2, dy2, r2 = calcular_radio(i2, p1)
    b2 = magnitud_campo(corriente2, r2)
    bx2, by2 = componentes_campo(corriente2,r2,dx2,dy2,"entrante")
    
    # Calculo para Btotal
    bx_total = bx1 + bx2
    by_total = by1 + by2
    b_total = magnitud_vector(bx_total,by_total)

    fig = visualizacion_resolucion_p1()
    fig2 = visualizacion_resolucion_i2() 
    
    return render_template(
        "tema2_resolucion_p1.html",
        grafico=fig.to_html(
            full_html=False,
            include_plotlyjs="cdn"
        ),
        grafico_i2=fig2.to_html(
            full_html=False,
            include_plotlyjs="cdn"
        ),
        dx1=dx1,dy1=dy1,r1=r1,b1=b1,bx1=bx1,by1=by1,
        dx2=dx2,dy2=dy2,r2=r2,b2=b2,bx2=bx2,by2=by2,
        bx_total=bx_total,by_total=by_total,b_total=b_total
    )