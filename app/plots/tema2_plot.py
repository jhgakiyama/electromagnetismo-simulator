from math import sqrt
import plotly.graph_objects as go


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

==========================================================
REGLAS DE DISEÑO - COLORES
==========================================================

Conductor I1
    Azul

Campo B1
    Azul

Componentes Bx1 - By1
    Azul punteado

----------------------------------------------------------

Conductor I2
    Rojo

Campo B2
    Rojo

Componentes Bx2 - By2
    Rojo punteado

----------------------------------------------------------

Campo Total

    Negro
    (Representa el resultado de todos los campos)

==========================================================
"""

COLOR_I1 = "royalblue"
COLOR_I2 = "firebrick"
COLOR_BTOTAL = "black"

SIMBOLO_CORRIENTE_ENTRANTE = "circle-x-open"
SIMBOLO_CORRIENTE_SALIENTE = "circle-dot"


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
            opacity=0.6 ,
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
            opacity=0.6,
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
