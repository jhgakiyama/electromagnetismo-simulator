from flask import render_template
from flask import Blueprint
from app.plots.tema2_plot_vista_concep1 import visualizacion_conceptual_2a
from app.plots.tema2_plot_vista_concep2 import visualizacion_conceptual_2b
from app.plots.tema2_plot import (
    visualizacion_ejercicio_2,
    visualizacion_resolucion_p1,
    visualizacion_resolucion_i2,
    visualizacion_resultado_final,
    visualizacion_autoevaluacion_p2
    )

from app.physics.tema2 import calcular_radio,magnitud_campo,componentes_campo,magnitud_vector


bp = Blueprint(
    "tema2",
    __name__
)

@bp.route("/tema2/demo/1")
def tema2_demo1():

    fig = visualizacion_conceptual_2a()

    return render_template(
        "tema2_demo.html",
        grafico=fig.to_html(
            full_html=False
        )
    )

@bp.route("/tema2/demo/2")
def tema2_demo2():

    fig = visualizacion_conceptual_2b()

    return render_template(
        "tema2_demo.html",
        grafico=fig.to_html(
            full_html=False
        )
    )

@bp.route("/tema2/ejercicio")
def ejercicio():
    fig_ejer = visualizacion_ejercicio_2()

    return render_template(
        "tema2_ejercicio.html",
        grafico=fig_ejer.to_html(
            full_html=False,
            include_plotlyjs="cdn"
        )
    )

@bp.route("/tema2")
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

    """" calcular_punto_p2 """
    p2 = (1.5, 0)

    # ----- Conductor I1 -----
    dx1_p2, dy1_p2, r1_p2 = calcular_radio(i1, p2)
    b1_p2 = magnitud_campo(corriente1, r1_p2)
    bx1_p2, by1_p2 = componentes_campo(corriente1,r1_p2,dx1_p2,dy1_p2,"entrante")

    # ----- Conductor I2 -----
    dx2_p2, dy2_p2, r2_p2 = calcular_radio(i2, p2)
    b2_p2 = magnitud_campo(corriente2, r2_p2)
    bx2_p2, by2_p2 = componentes_campo(corriente2,r2_p2,dx2_p2,dy2_p2,"entrante")

    # ----- Campo total -----

    bx_total_p2 = bx1_p2 + bx2_p2
    by_total_p2 = by1_p2 + by2_p2

    b_total_p2 = magnitud_vector(bx_total_p2,by_total_p2)

    # ----- Gráfico -----

    grafico_p2 = visualizacion_autoevaluacion_p2()

    # Le paso todas las graficas
    fig_concep_1 = visualizacion_conceptual_2a()
    fig_concep_2 = visualizacion_conceptual_2b()
    
    fig_ejer = visualizacion_ejercicio_2()
    fig = visualizacion_resolucion_p1()
    fig2 = visualizacion_resolucion_i2() 
    fig_resultado = visualizacion_resultado_final()

    return render_template(
        "tema2_resolucion_p1.html",
        grafico_conceptual_2a=fig_concep_1.to_html(
            full_html=False,
            include_plotlyjs="cdn"
        ),
        grafico_conceptual_2b=fig_concep_2.to_html(
            full_html=False,
            include_plotlyjs="cdn"
        ),
        grafico_ejer=fig_ejer.to_html(
            full_html=False,
            include_plotlyjs=False
        ),
        grafico=fig.to_html(
            full_html=False,
            include_plotlyjs=False
        ),
        grafico_i2=fig2.to_html(
            full_html=False,
            include_plotlyjs=False
        ),
        grafico_resultado=fig_resultado.to_html(
            full_html=False,
            include_plotlyjs=False
        ),
        dx1=dx1,dy1=dy1,r1=r1,b1=b1,bx1=bx1,by1=by1,
        dx2=dx2,dy2=dy2,r2=r2,b2=b2,bx2=bx2,by2=by2,
        bx_total=bx_total,by_total=by_total,b_total=b_total,

        #Agrego todo los puntos para el calculo de P2
        r1_p2=r1_p2,r2_p2=r2_p2,b1_p2=b1_p2,b2_p2=b2_p2,
        bx_total_p2=bx_total_p2,by_total_p2=by_total_p2,b_total_p2=b_total_p2,

        grafico_p2=grafico_p2.to_html(full_html=False,include_plotlyjs=False)
    )