from math import sqrt
import plotly.graph_objects as go
from app.physics.tema2 import normalizar_vector, escalar_vector
from app.plots.tema2_plot import dibujar_vector, dibujar_radio,visualizacion_ejercicio_2


COLOR_I1 = "#d62728"
COLOR_I2 = "#1f77b4"
COLOR_RESULTANTE = "#2ca02c"


def visualizacion_resultado_laboratorio(resultado):

    # ==========================================================
    # ETAPA 1 - Desempaquetar resultado
    # ==========================================================

    param = resultado["parametros"]
    geo = resultado["geometria"]

    b1 = resultado["b1"]
    b2 = resultado["b2"]
    campo = resultado["campo_total"]

    # ----------------------------------------------------------
    # Parámetros
    # ----------------------------------------------------------

    corriente1 = param["corriente1"]
    corriente2 = param["corriente2"]

    sentido1 = param["sentido1"]
    sentido2 = param["sentido2"]

    # ----------------------------------------------------------
    # Geometría
    # ----------------------------------------------------------

    x1, y1 = geo["conductor1"]
    x2, y2 = geo["conductor2"]

    px, py = geo["p"]

    r1 = geo["r1"]
    r2 = geo["r2"]

    dx1 = geo["dx1"]
    dy1 = geo["dy1"]

    dx2 = geo["dx2"]
    dy2 = geo["dy2"]

    # ----------------------------------------------------------
    # Campo B1
    # ----------------------------------------------------------

    bx1 = b1["bx"]
    by1 = b1["by"]
    b1_mag = b1["magnitud"]

    # ----------------------------------------------------------
    # Campo B2
    # ----------------------------------------------------------

    bx2 = b2["bx"]
    by2 = b2["by"]
    b2_mag = b2["magnitud"]

    # ----------------------------------------------------------
    # Campo resultante
    # ----------------------------------------------------------

    bx = campo["bx"]
    by = campo["by"]
    btotal = campo["magnitud"]


    # ==========================================================
    # ETAPA 2 - Preparar vectores para dibujar
    # ==========================================================

    bx1_g, by1_g = normalizar_vector(bx1, by1)
    bx2_g, by2_g = normalizar_vector(bx2, by2)
    bx_g,  by_g  = normalizar_vector(bx, by)

    bx1_g, by1_g = escalar_vector(bx1_g, by1_g, 0.45)
    bx2_g, by2_g = escalar_vector(bx2_g, by2_g, 0.45)
    bx_g,  by_g  = escalar_vector(bx_g,  by_g,  0.45)


    # ==========================================================
    # ETAPA 3 - Crear figura base
    # ==========================================================

    fig = visualizacion_ejercicio_2()


    # ==========================================================
    # ETAPA 4 - Dibujar geometría
    # ==========================================================

    dibujar_radio(fig=fig,origen_x=x1,origen_y=y1,destino_x=px,destino_y=py,etiqueta="r1",color=COLOR_I1)
    dibujar_radio(fig=fig,origen_x=x2,origen_y=y2,destino_x=px,destino_y=py,etiqueta="r2",color=COLOR_I2)

    # ==========================================================
    # ETAPA 5 - Dibujar campos magnéticos
    # ==========================================================

    dibujar_vector(fig=fig,origen_x=px,origen_y=py,vx=bx1_g,vy=by1_g,etiqueta="B1",color=COLOR_I1)

    dibujar_vector(fig=fig,origen_x=px,origen_y=py,vx=bx2_g,vy=by2_g,etiqueta="B2",color=COLOR_I2)

    dibujar_vector(fig=fig,origen_x=px,origen_y=py,vx=bx_g,vy=by_g,etiqueta="B",color=COLOR_RESULTANTE)

    # ==========================================================
    # ETAPA 6 - Layout
    # ==========================================================

    fig.update_layout(title="Laboratorio Virtual - Campo Magnético Resultante",showlegend=False)

    # ==========================================================
    # ETAPA 7 - Resultado
    # ==========================================================

    return fig