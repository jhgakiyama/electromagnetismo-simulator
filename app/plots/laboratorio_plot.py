from math import sqrt
import plotly.graph_objects as go
from app.plots.tema2_plot import normalizar_vector,dibujar_vector, dibujar_radio,visualizacion_ejercicio_2, escalar_vector
from app.plots.elementos import dibujar_conductor, dibujar_punto


COLOR_I1 = "#d62728"
COLOR_I2 = "#1f77b4"
COLOR_P = "#444444"
COLOR_RESULTANTE = "#2ca02c"


def visualizacion_laboratorio_base():
    """ Genera un grafico base. """

    fig = go.Figure()
    
    # Dibujo los ejes
    fig.update_xaxes(
        title="X (cm)",
        showgrid=True
    )

    fig.update_yaxes(
        title="Y (cm)",
        scaleanchor="x",
        scaleratio=1,
        showgrid=True
    )

    # Marco el eje X & Y
    fig.add_hline(y=0,line_color="black",line_width=2)
    fig.add_vline(x=0,line_color="black",line_width=2)

    return fig

def visualizacion_resultado_laboratorio(resultado):
    """
    Recibe el objeto resultado ya calculado y genera la representación visual del experimento.
    
    """
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

    fig = visualizacion_laboratorio_base()

    # ==========================================================
    # ETAPA 4 - Dibujar geometría
    # ==========================================================

    dibujar_radio(fig=fig,origen_x=x1,origen_y=y1,destino_x=px,destino_y=py,etiqueta="r1",color=COLOR_I1)
    dibujar_radio(fig=fig,origen_x=x2,origen_y=y2,destino_x=px,destino_y=py,etiqueta="r2",color=COLOR_I2)

    # ==========================================================
    # ETAPA 4.1 - Dibujar conductores
    # ==========================================================

    dibujar_conductor(fig=fig,x=x1,y=y1,sentido=sentido1,etiqueta="I₁",color=COLOR_I1)
    dibujar_conductor(fig=fig,x=x2,y=y2,sentido=sentido2,etiqueta="I₂",color=COLOR_I2)

    # ==========================================================
    # ETAPA 5 - Dibujar campos magnéticos
    # ==========================================================

    dibujar_vector(fig=fig,origen_x=px,origen_y=py,vx=bx1_g,vy=by1_g,etiqueta="B1",color=COLOR_I1)
    dibujar_vector(fig=fig,origen_x=px,origen_y=py,vx=bx2_g,vy=by2_g,etiqueta="B2",color=COLOR_I2)

    dibujar_vector(fig=fig,origen_x=px,origen_y=py,vx=bx_g,vy=by_g,etiqueta="B",color=COLOR_RESULTANTE)

    # ==========================================================
    # ETAPA 5.1 - Dibujar punto de observacion
    # ==========================================================

    dibujar_punto(fig,px,py,"P",COLOR_P)

    # ==========================================================
    # ETAPA 6 - Layout
    # ==========================================================

    fig.update_layout(
        title="Laboratorio Virtual - Campo Magnético Resultante",
        template="plotly",
        showlegend=False)
    

    # Calculos valores minimos y maximos para los ejes

    x_min = min(x1, x2, px) - 1
    x_max = max(x1, x2, px) + 1

    y_min = min(y1, y2, py) - 1
    y_max = max(y1, y2, py) + 1

    fig.update_xaxes(range=[x_min, x_max])
    fig.update_yaxes(range=[y_min, y_max])
    # ==========================================================
    # ETAPA 7 - Resultado
    # ==========================================================

    return fig