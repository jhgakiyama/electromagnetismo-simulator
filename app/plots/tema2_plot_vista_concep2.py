from math import sqrt
import plotly.graph_objects as go
from app.physics.tema2 import vector_perpendicular
from app.plots.tema2_plot import *


def visualizacion_conceptual_2b():
    """
    Objetivo:
        Mostrar un caso de simetría donde algunas
        componentes del campo magnético se cancelan.

    Retorna:
        Figura Plotly.

    Notas:
        Permite visualizar la cancelación de
        componentes y el campo resultante.
    """
    # Longitud fijo
    L2 = 0.5

    # Defino valores fijos
    # I1
    i1_x = -1
    i1_y = 0
    
    # I2
    i2_x = 1
    i2_y = 0

    # P
    p_x = 0
    p_y = 1

    fig = go.Figure()

    # Dibujo para I1
    fig.add_trace(
        go.Scatter(
            x=[i1_x],
            y=[i1_y],
            text=["I1"],
            textposition="top center",
            name="I1 = (-1,0)",
            marker=dict(
                symbol=SIMBOLO_CORRIENTE_ENTRANTE,
                size=14,
                color="blue",
                line=dict(width=2)
            )
        )
    )

    # Dibujo para I2
    fig.add_trace(
        go.Scatter(
            x=[i2_x],
            y=[i2_y],
            text=["I2"],
            textposition="top center",
            name="I2 = (1,0)",
            marker=dict(
                symbol=SIMBOLO_CORRIENTE_ENTRANTE,
                size=14,
                color="red",
                line=dict(width=2)
            )
        )
    )

    # Dibujo para P
    fig.add_trace(
        go.Scatter(
            x=[p_x],
            y=[p_y],
            mode="markers+text",
            text=["P"],
            textposition="top left",
            name="P = (0.5,1)"
        )
    )

    # textposition = ['top left', 'top center', 'top right', 
    # 'middle left','middle center', 'middle right', 
    # 'bottom left', 'bottom center', 'bottom right']


    # Distancia I1 → P r1
    fig.add_trace(
        go.Scatter(
            x=[i1_x, p_x],
            y=[i1_y, p_y],
            mode="lines",
            line=dict(dash="dot"),
            showlegend=False,
            hoverinfo="skip"
        )
    )

    # Distancia I2 → P r2
    fig.add_trace(
        go.Scatter(
            x=[i2_x, p_x],
            y=[i2_y, p_y],
            mode="lines",
            line=dict(dash="dot"),
            showlegend=False,
            hoverinfo="skip"
        )
    )

    ''' Hago los calculos geometricos para B1 '''
     # Calculo Vector Radio
    dx1 = p_x - i1_x
    dy1 = p_y - i1_y

    # Direccion de B
    bx1, by1 = vector_perpendicular(dx1,dy1,"entrante")
    # Normalizo
    bx1, by1 = normalizar_vector(bx1,by1)

    # Prueba de Longitud final   
    bx1 *= L2
    by1 *= L2

    '''FIN CALCULOS B1'''

    # Agrego para vector de B1
    fig.add_annotation(
        x=p_x + bx1,
        y=p_y + by1,
        # Agrego porque no se ven los vectores
        xref="x",
        yref="y",

        ax=p_x,
        ay=p_y,

        # Agrego porque no se ven los vectores
        axref="x",
        ayref="y",
        
        showarrow=True,
        arrowhead=3,
        arrowwidth=3,
        arrowcolor=COLOR_I1,
        text=""
    )

    fig.add_trace(
        go.Scatter(
            x=[p_x + bx1 * 0.6],
            y=[p_y + by1 * 0.6],
            mode="text",
            text=["B1"],
            showlegend=False,
            textposition="middle right",
            textfont=dict(color=COLOR_I1)
        )
    )

    ''' Hago los calculos geometricos para B2 '''
     # Calculo Vector Radio
    dx2 = p_x - i2_x
    dy2 = p_y - i2_y

    # Direccion de B2
    bx2, by2 = vector_perpendicular(dx2,dy2,"entrante")

    # Normalizo
    bx2, by2 = normalizar_vector(bx2,by2)

    bx2 *= L2
    by2 *= L2
    '''FIN CALCULOS B2'''

    # Agrego para vector de B2
    fig.add_annotation(
        x=p_x + bx2,
        y=p_y + by2,
        ax=p_x,
        ay=p_y,
        # Agrego porque no se ven los vectores
        xref="x",
        yref="y",
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=3,
        arrowwidth=3,
        arrowcolor=COLOR_I2
    )

    fig.add_trace(
        go.Scatter(
            x=[p_x + bx2 * 0.6],
            y=[p_y + by2 * 0.6],
            mode="text",
            text=["B2"],
            showlegend=False,
            textposition="middle left",
            textfont=dict(color=COLOR_I2)
        )
    )
    # Calculo para Btotal
    bx_total = bx1 + bx2
    by_total = by1 + by2

    # Agrego vector Btotal
    fig.add_annotation(
        x=p_x + bx_total,
        y=p_y + by_total,       
        ax=p_x,
        ay=p_y,
        # Agrego porque no se ven los vectores
        xref="x",
        yref="y",
        axref="x",
        ayref="y",

        showarrow=True,
        arrowhead=3,
        arrowwidth=3,
        arrowcolor=COLOR_BTOTAL,
        text="",
        font=dict(color=COLOR_BTOTAL)
    )

    fig.add_trace(
        go.Scatter(
            x=[p_x + bx_total * 0.6],
            y=[p_y + by_total * 0.6],
            mode="text",
            text=["Btotal"],
            showlegend=False,
            textposition="top center"
        )
    )

    # Dibujo para Bx1 - By1
    dibujar_componentes_vector(fig,p_x,p_y,bx1,by1,"Bx1","By1",color=COLOR_I1)

    # Dibujo para Bx2 - By2
    dibujar_componentes_vector(fig,p_x,p_y,bx2,by2,"Bx2","By2",color=COLOR_I2)

    # Se ve mejor los ejes
    fig.update_xaxes(zeroline=True,showgrid=False)
    fig.update_yaxes(zeroline=True,showgrid=False,scaleanchor="x",scaleratio=1)
    fig.update_layout(title="Visualización Conceptual 2B - Caso Simétrico",showlegend=True)

    return fig
