from math import sqrt
import plotly.graph_objects as go
from app.physics.tema2 import vector_perpendicular


"""
REGLAS PARA LOS GRAFICOS
Conductores:
I1 (rojo)
I2 (azul)

Punto:
P (verde)

Vectores visibles:
B1 - B2 - Btotal

Ayuda visual:
Líneas punteadas

Sin números - Sin coordenadas - Sin fórmulas
"""


def normalizar_vector(x, y):
    """
    Objetivo:
        Obtener un vector unitario a partir de un vector cualquiera.

    Parámetros:
        x: componente X
        y: componente Y

    Retorna:
        ux: componente X normalizada
        uy: componente Y normalizada
    """

    norma = sqrt(x**2 + y**2)

    return x / norma, y / norma


def visualizacion_conceptual_2a():
    """
    Objetivo:
        Mostrar la suma vectorial de los campos
        magnéticos B1 y B2 sobre un punto de observación.

    Retorna:
        Figura Plotly.

    Notas:
        Es una visualización conceptual.

        Utiliza valores genéricos para facilitar
        la comprensión de la superposición de campos.
    """
    # Longitud fijo
    L = 0.5

    # Defino valores fijos
    # I1
    i1_x = -1 ,i1_y = 0
    
    # I2
    i2_x = 1, i2_y = 0

    # P
    p_x = 0.5, p_y = 1

    fig = go.Figure()

    # Dibujo para I1
    fig.add_trace(
        go.Scatter(
            x=[i1_x],
            y=[i1_y],
            mode="markers+text",
            text=["I1"],
            textposition="top center",
            name="I1"
        )
    )

    # Dibujo para I2
    fig.add_trace(
        go.Scatter(
            x=[i2_x],
            y=[i2_y],
            mode="markers+text",
            text=["I2"],
            textposition="top center",
            name="I2"
        )
    )

    # Dibujo para P
    fig.add_trace(
        go.Scatter(
            x=[p_x],
            y=[p_y],
            mode="markers+text",
            text=["P"],
            textposition="top center",
            name="P"
        )
    )

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

    # Se ve mejor los ejes
    fig.update_xaxes(
        zeroline=True,
        showgrid=False
    )

    fig.update_yaxes(
        zeroline=True,
        showgrid=False,
        scaleanchor="x",
        scaleratio=1
    )

    fig.update_layout(title="Visualización Conceptual 2A - Superposición de Campos",showlegend=True)

    ''' Hago los calculos geometricos para B1 '''
     # Calculo Vector Radio
    dx1 = p_x - i1_x
    dy1 = p_y - i1_y

    # Direccion de B
    bx1, by1 = vector_perpendicular(dx1,dy1,"entrante")
    # Normalizo
    bx1, by1 = normalizar_vector(bx1,by1)

    # Prueba de Longitud final   
    bx1 *= L
    by1 *= L

    '''FIN CALCULOS B1'''

    # Agrego para vector de B1
    fig.add_annotation(
        x=p_x + bx1,
        y=p_y + by1,
        ax=p_x,
        ay=p_y,
        showarrow=True,
        arrowhead=3,
        arrowwidth=1,
        text="B1"
    )

    ''' Hago los calculos geometricos para B1 '''
     # Calculo Vector Radio
    dx2 = p_x - i2_x
    dy2 = p_y - i2_y

    # Direccion de B1
    bx2, by2 = vector_perpendicular(dx2,dy2,"entrante")

    # Normalizo
    bx2, by2 = normalizar_vector(bx2,by2)

    bx2 *= L 
    by2 *= L
    '''FIN CALCULOS B2'''

    # Agrego para vector de B2
    fig.add_annotation(
        x=p_x + bx2,
        y=p_y + by2,
        ax=p_x,
        ay=p_y,
        showarrow=True,
        arrowhead=3,
        arrowwidth=1,
        text="B2"
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
        showarrow=True,
        arrowhead=3,
        arrowwidth=3,
        text="Btotal"
    )

    return fig


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
    pass

def visualizacion_conceptual_2c():
    """
    Objetivo:
        Mostrar un caso general donde los campos
        producidos por los conductores poseen
        diferentes magnitudes y direcciones.

    Retorna:
        Figura Plotly.

    Notas:
        Permite visualizar cómo la geometría
        influye sobre el campo magnético total.
    """
    pass