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


# Responsabilidades:
# Calcular el punto intermedio.
# Dibujar la componente vertical.
# Dibujar la componente horizontal.
# Agregar las etiquetas.
def dibujar_componentes_vector(
    fig,
    origen_x,
    origen_y,
    comp_x,
    comp_y,
    etiqueta_x,
    etiqueta_y,
    color="deeppink",
    dash="dot"
):
    """
    Objetivo:
        Dibujar la descomposición ortogonal de un vector
        mediante sus componentes horizontal y vertical.

    Parámetros:
        fig:
            Figura Plotly.

        origen_x:
            Coordenada X del origen del vector.

        origen_y:
            Coordenada Y del origen del vector.

        comp_x:
            Componente horizontal.

        comp_y:
            Componente vertical.

        etiqueta_x:
            Nombre de la componente horizontal.

        etiqueta_y:
            Nombre de la componente vertical.

        color:
            Color de las líneas auxiliares.

        dash:
            Estilo de línea (dot, dash, etc.).

    Retorna:
        None.

    Notas:
        La construcción utilizada es:

            Vertical
                ↓
            Horizontal
    """

    # ==========================================================
    # Componente vertical
    # ==========================================================

    fig.add_trace(
        go.Scatter(
            x=[origen_x, origen_x],
            y=[origen_y, origen_y + comp_y],
            mode="lines",
            line=dict(
                color=color,
                dash=dash
            ),
            showlegend=False,
            hoverinfo="skip"
        )
    )

    # ==========================================================
    # Componente horizontal
    # ==========================================================

    fig.add_trace(
        go.Scatter(
            x=[origen_x, origen_x + comp_x],
            y=[origen_y + comp_y, origen_y + comp_y],
            mode="lines",
            line=dict(
                color=color,
                dash=dash
            ),
            showlegend=False,
            hoverinfo="skip"
        )
    )

    # ==========================================================
    # Etiqueta componente vertical
    # ==========================================================

    fig.add_trace(
        go.Scatter(
            x=[origen_x - 0.05],
            y=[origen_y + comp_y / 2],
            mode="text",
            text=[etiqueta_y],
            showlegend=False,
            hoverinfo="skip"
        )
    )

    # ==========================================================
    # Etiqueta componente horizontal
    # ==========================================================

    fig.add_trace(
        go.Scatter(
            x=[origen_x + comp_x / 2],
            y=[origen_y + comp_y + 0.03],
            mode="text",
            text=[etiqueta_x],
            showlegend=False,
            hoverinfo="skip"
        )
    )


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
    L1 = 0.5

    # Defino valores fijos
    # I1
    i1_x = -1
    i1_y = 0
    
    # I2
    i2_x = 1
    i2_y = 0

    # P
    p_x = 0.5
    p_y = 1

    fig = go.Figure()

    # Dibujo para I1
    fig.add_trace(
        go.Scatter(
            x=[i1_x],
            y=[i1_y],
            mode="markers+text",
            text=["I1"],
            textposition="top center",
            name="I1 = (-1,0)"
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
            name="I2 = (1,0)"
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
            name="P = (0.5,1)"
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

    ''' Hago los calculos geometricos para B1 '''
     # Calculo Vector Radio
    dx1 = p_x - i1_x
    dy1 = p_y - i1_y

    # Direccion de B
    bx1, by1 = vector_perpendicular(dx1,dy1,"entrante")
    # Normalizo
    bx1, by1 = normalizar_vector(bx1,by1)

    # Prueba de Longitud final   
    bx1 *= L1
    by1 *= L1

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
        text=""
    )

    fig.add_trace(
        go.Scatter(
            x=[p_x + bx1 * 0.6],
            y=[p_y + by1 * 0.6],
            mode="text",
            text=["B1"],
            showlegend=False,
            textposition="middle right"
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

    bx2 *= L1 
    by2 *= L1
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
    )

    fig.add_trace(
        go.Scatter(
            x=[p_x + bx2 * 0.6],
            y=[p_y + by2 * 0.6],
            mode="text",
            text=["B2"],
            showlegend=False,
            textposition="middle left"
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
        text=""
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

    # Se ve mejor los ejes
    fig.update_xaxes(zeroline=True,showgrid=False)
    fig.update_yaxes(zeroline=True,showgrid=False,scaleanchor="x",scaleratio=1)
    fig.update_layout(title="Visualización Conceptual 2A - Superposición de Campos",showlegend=True)

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
            mode="markers+text",
            text=["I1"],
            textposition="top center",
            name="I1 = (-1,0)"
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
            name="I2 = (1,0)"
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
            name="P = (0.5,1)"
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
        text=""
    )

    fig.add_trace(
        go.Scatter(
            x=[p_x + bx1 * 0.6],
            y=[p_y + by1 * 0.6],
            mode="text",
            text=["B1"],
            showlegend=False,
            textposition="middle right"
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
    )

    fig.add_trace(
        go.Scatter(
            x=[p_x + bx2 * 0.6],
            y=[p_y + by2 * 0.6],
            mode="text",
            text=["B2"],
            showlegend=False,
            textposition="middle left"
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
        text=""
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
    dibujar_componentes_vector(fig,p_x,p_y,bx1,by1,"Bx1","By1")

    # Dibujo para Bx2 - By2
    dibujar_componentes_vector(fig,p_x,p_y,bx2,by2,"Bx2","By2")

    # Se ve mejor los ejes
    fig.update_xaxes(zeroline=True,showgrid=False)
    fig.update_yaxes(zeroline=True,showgrid=False,scaleanchor="x",scaleratio=1)
    fig.update_layout(title="Visualización Conceptual 2B - Caso Simétrico",showlegend=True)

    return fig

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