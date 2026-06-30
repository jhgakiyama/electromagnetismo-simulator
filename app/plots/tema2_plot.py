from math import sqrt
import plotly.graph_objects as go
from app.physics.tema2 import componentes_campo, calcular_radio


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

COLOR_I1 = "firebrick"
COLOR_I2 = "royalblue"
COLOR_BTOTAL = "black"

SIMBOLO_CORRIENTE_ENTRANTE = "circle-x-open"
SIMBOLO_CORRIENTE_SALIENTE = "circle-dot"


def normalizar_vector(x, y, longitud=0.8):
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


def escalar_vector(x, y, longitud=1):
    """
    Objetivo:
        Escalar un vector unitario a la longitud deseada.

    Parámetros:
        x: componente X del vector unitario.
        y: componente Y del vector unitario.
        longitud: longitud deseada.

    Retorna:
        x_escalado
        y_escalado
    """

    return x * longitud, y * longitud


def dibujar_vector(fig,origen_x,origen_y,vx,vy,etiqueta,color,arrowwidth=2,textposition="top center"):
    """
    Objetivo:
        Dibujar un vector sobre una figura Plotly.

    Parámetros:
        fig:
            Figura Plotly.

        origen_x, origen_y:
            Coordenadas del origen del vector.

        vx, vy:
            Componentes del vector.

        etiqueta:
            Texto identificador del vector.

        color:
            Color del vector y de la etiqueta.

        textposition:
            Posición de la etiqueta respecto del extremo
            del vector.

    Retorna:
        None.

    Notas:
        Esta función únicamente representa el vector.
        No realiza cálculos físicos.
    """

    destino_x = origen_x + vx
    destino_y = origen_y + vy

    texto_x = origen_x + vx * 0.60
    texto_y = origen_y + vy * 0.60

    # Flecha
    fig.add_annotation(
        x=destino_x,
        y=destino_y,
        ax=origen_x,
        ay=origen_y,
        xref="x",
        yref="y",
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=3,
        arrowsize=1,
        arrowwidth=arrowwidth,
        arrowcolor=color
    )

    # Etiqueta
    fig.add_trace(
        go.Scatter(
            x=[texto_x],
            y=[texto_y],
            mode="text",
            text=[etiqueta],
            textfont=dict(
                color=color,
                size=11
            ),
            textposition=textposition,
            showlegend=False,
            hoverinfo="skip"
        )
    )

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

    # Componente vertical
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

    # Componente horizontal
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

    # Etiqueta componente vertical
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

    # Etiqueta componente horizontal
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


def dibujar_radio(fig,origen_x,origen_y,destino_x,destino_y,etiqueta,color,textposition="middle center",estilo_linea="dot"):
    """
    Objetivo:
        Dibujar el vector radio entre un conductor y un
        punto de observación.

    Parámetros:
        fig:
            Figura Plotly.

        origen_x, origen_y:
            Coordenadas del conductor.

        destino_x, destino_y:
            Coordenadas del punto de observación.

        etiqueta:
            Nombre del radio (r1, r2, etc.).

        color:
            Color de la línea y de la etiqueta.

        textposition:
            Posición de la etiqueta respecto del punto
            medio del radio.

    Retorna:
        None.

    Notas:
        El radio se representa mediante una línea
        punteada. No realiza ningún cálculo físico.
    """

    # Línea del radio
    fig.add_trace(
        go.Scatter(
            x=[origen_x, destino_x],
            y=[origen_y, destino_y],
            mode="lines",
            line=dict(
                color=color,
                width=2,
                dash=estilo_linea
            ),
            showlegend=False,
            hoverinfo="skip"
        )
    )

    # Punto medio para la etiqueta
    medio_x = (origen_x + destino_x) / 2
    medio_y = (origen_y + destino_y) / 2

    medio_y *= 1.1

    # Etiqueta
    fig.add_trace(
        go.Scatter(
            x=[medio_x],
            y=[medio_y],
            mode="text",
            text=[etiqueta],
            textfont=dict(
                color=color,
                size=12
            ),
            textposition=textposition,
            showlegend=False,
            hoverinfo="skip"
        )
    )

def visualizacion_base_ejercicio_2():
    # Conductores
    i1_x = 0
    i1_y = 0

    i2_x = 2
    i2_y = 0

    # Puntos de observación
    p1_x = 1
    p1_y = 1

    fig = go.Figure()

    # Conductor I1
    fig.add_trace(
        go.Scatter(
            x=[i1_x],
            y=[i1_y],
            mode="markers+text",
            marker=dict(
                symbol=SIMBOLO_CORRIENTE_ENTRANTE,
                size=14,
                color=COLOR_I1
            ),
            text=["I1"],
            textposition="top center",
            showlegend=False,
            hoverinfo="skip"
        )
    )

    # Conductor I2
    fig.add_trace(
        go.Scatter(
            x=[i2_x],
            y=[i2_y],
            mode="markers+text",
            marker=dict(
                symbol=SIMBOLO_CORRIENTE_ENTRANTE,
                size=14,
                color=COLOR_I2
            ),
            text=["I2"],
            textposition="top center",
            showlegend=False,
            hoverinfo="skip"
        )
    )

    # Punto P1
    fig.add_trace(
        go.Scatter(
            x=[p1_x],
            y=[p1_y],
            mode="markers+text",
            marker=dict(
                symbol="circle",
                size=8,
                color="green"
            ),
            text=["P1"],
            textposition="top center",
            showlegend=False,
            hoverinfo="skip"
        )
    )

    # Layout
    fig.update_layout(title="Geometría del Problema",template="plotly",height=550,margin=dict(l=40, r=40, t=60, b=40))

    # Actualizo parametros para los ejer X e Y
    fig.update_xaxes(range=[0, 2.5],showgrid=False,zeroline=False,scaleanchor="y")
    fig.update_yaxes(range=[-0.5, 1.5],showgrid=False,zeroline=False)

    # Eje X
    fig.add_shape(type="line",x0=-1.5,y0=0,x1=5,y1=0,line=dict(color="black",width=1))

    # Eje Y
    fig.add_shape(type="line",x0=0,y0=-0.5,x1=0,y1=1.5,line=dict(color="black",width=1))

    return fig


def visualizacion_ejercicio_2():
    """
    Objetivo:
        Representar la geometría del ejercicio resuelto.

    Retorna:
        Figura Plotly.

    Notas:
        Representa únicamente:

        - Conductores.
        - Puntos de observación.
        - Separación entre conductores.

        No realiza cálculos físicos.
    """

    # Conductores
    i1_x = 0
    i1_y = 0

    i2_x = 2
    i2_y = 0

    # Puntos de observación
    p1_x = 1
    p1_y = 1

    p2_x = 1.5
    p2_y = 0

    fig = go.Figure()

    # Conductor I1
    fig.add_trace(
        go.Scatter(
            x=[i1_x],
            y=[i1_y],
            mode="markers+text",
            marker=dict(
                symbol=SIMBOLO_CORRIENTE_ENTRANTE,
                size=14,
                color=COLOR_I1
            ),
            text=["I1"],
            textposition="top center",
            showlegend=False,
            hoverinfo="skip"
        )
    )

    # Conductor I2
    fig.add_trace(
        go.Scatter(
            x=[i2_x],
            y=[i2_y],
            mode="markers+text",
            marker=dict(
                symbol=SIMBOLO_CORRIENTE_ENTRANTE,
                size=14,
                color=COLOR_I2
            ),
            text=["I2"],
            textposition="top center",
            showlegend=False,
            hoverinfo="skip"
        )
    )

    # Punto P1
    fig.add_trace(
        go.Scatter(
            x=[p1_x],
            y=[p1_y],
            mode="markers+text",
            marker=dict(
                symbol="circle",
                size=8,
                color="green"
            ),
            text=["P1"],
            textposition="top center",
            showlegend=False,
            hoverinfo="skip"
        )
    )

    # Punto P2
    fig.add_trace(
        go.Scatter(
            x=[p2_x],
            y=[p2_y],
            mode="markers+text",
            marker=dict(
                symbol="circle",
                size=6,
                color="palegreen"
            ),
            text=["P2"],
            textposition="middle right",
            showlegend=False,
            hoverinfo="skip"
        )
    )

    # Separación entre conductores
    fig.add_shape(type="line",x0=i1_x,y0=-0.125,x1=i2_x,y1=-0.125,line=dict(color="gray",dash="dot"))
    fig.add_annotation(x=1,y=-0.2,text="d = 2 cm",showarrow=False,font=dict(size=12))

    # Layout
    fig.update_layout(title="Geometría del Problema",template="plotly",height=550,margin=dict(l=40, r=40, t=60, b=40))

    # Actualizo parametros para los ejer X e Y
    fig.update_xaxes(range=[0, 2.5],showgrid=False,zeroline=False,scaleanchor="y")
    fig.update_yaxes(range=[-0.5, 1.5],showgrid=False,zeroline=False)

    # Eje X
    fig.add_shape(type="line",x0=-1.5,y0=0,x1=5,y1=0,line=dict(color="black",width=1))

    # Eje Y
    fig.add_shape(type="line",x0=0,y0=-0.5,x1=0,y1=1.5,line=dict(color="black",width=1))
    return fig


def visualizacion_resolucion_p1():
    """
    Objetivo:
        Representar el primer paso de la resolución del ejercicio
        mostrando los campos magnéticos generados por cada conductor
        sobre el punto P1.

    Retorna:
        go.Figure

    Notas:
        Muestra:
            - Conductores.
            - Punto P1.
            - Campo B1.
            - Campo B2.

        No muestra:
            - Componentes.
            - Campo total.
            - Resultados numéricos.
    """
    i1 = (0, 0)
    i2 = (2, 0)
    p1 = (1, 1)
    corriente1 = 1
    corriente2 = 1

    # Cálculo de los campos
    # Conductor I1 -> P1
    dx1, dy1, r1 = calcular_radio(i1,p1)
    bx1, by1 = componentes_campo(corriente1,r1,dx1,dy1,"entrante")
    
    # Conductor I2 -> P1

    dx2, dy2, r2 = calcular_radio(i2,p1)
    bx2, by2 = componentes_campo(corriente2,r2,dx2,dy2,"entrante")

    # Solo para representación gráfica
    bx1, by1 = normalizar_vector(bx1, by1)
    bx2, by2 = normalizar_vector(bx2, by2)
    
    # Escalo el vector en 0.5, sino sale del layout
    bx1, by1 = escalar_vector(bx1, by1, 0.5)
    bx2, by2 = escalar_vector(bx2, by2, 0.5)

    fig = visualizacion_ejercicio_2()

    # Vector B1
    dibujar_vector(
        fig=fig,
        origen_x=p1[0],
        origen_y=p1[1],
        vx=bx1,
        vy=by1,
        etiqueta="B1",
        color=COLOR_I1
    )

    # Dibujo la distancia entre I1 y P1 >> r1
    dibujar_radio(
        fig=fig,
        origen_x=i1[0],
        origen_y=i1[1],
        destino_x=p1[0],
        destino_y=p1[1],
        etiqueta="r1",
        color=COLOR_I1
    )

    # Vector B2
    dibujar_vector(
        fig=fig,
        origen_x=p1[0],
        origen_y=p1[1],
        vx=bx2,
        vy=by2,
        etiqueta="B2",
        color=COLOR_I2
    )

    # Dibujo la distancia entre I2 y P2 >> r2
    dibujar_radio(
        fig=fig,
        origen_x=i2[0],
        origen_y=i2[1],
        destino_x=p1[0],
        destino_y=p1[1],
        etiqueta="r2",
        color=COLOR_I2
    )

    dibujar_componentes_vector(
        fig=fig,
        origen_x=p1[0],origen_y=p1[1],
        comp_x=bx1,comp_y=by1,
        etiqueta_x="Bx1",
        etiqueta_y="By1",
        color=COLOR_I1
)
    # Layout
    fig.update_layout(title="Descomposicion vectorial de B1")

    return fig

def visualizacion_resolucion_i2():
    """
    Esta funcion deberia ser un espejo a la anterior
    Solo que para calcular los valores asociados a B2
    """
    
    i1 = (0, 0)
    i2 = (2, 0)

    p1 = (1, 1)

    corriente1 = 1
    corriente2 = 1

    # Conductor I1 -> P1
    dx1, dy1, r1 = calcular_radio(i1,p1)
    bx1, by1 = componentes_campo(corriente1,r1,dx1,dy1,"entrante")
    
    # Conductor I2 -> P1

    dx2, dy2, r2 = calcular_radio(i2,p1)
    bx2, by2 = componentes_campo(corriente2,r2,dx2,dy2,"entrante")

    # Solo para representación gráfica
    bx1, by1 = normalizar_vector(bx1, by1)
    bx2, by2 = normalizar_vector(bx2, by2)
    
    # Escalo el vector en 0.5, sino sale del layout
    bx1, by1 = escalar_vector(bx1, by1, 0.5)
    bx2, by2 = escalar_vector(bx2, by2, 0.5)

    fig = visualizacion_ejercicio_2()

    # B1 NO es el protagonista en este grafico, se le baja el color
    dibujar_vector(
        fig=fig,
        origen_x=p1[0],
        origen_y=p1[1],
        vx=bx1,
        vy=by1,
        etiqueta="B1",
        color="rgba(220,0,0,0.35)"
    )

    # r1 NO es el protagonista en este grafico, se le baja el color
    dibujar_radio(
        fig=fig,
        origen_x=i1[0],
        origen_y=i1[1],
        destino_x=p1[0],
        destino_y=p1[1],
        etiqueta="r1",
        color="rgba(220,0,0,0.35)"
    )

    # Vector B2
    dibujar_vector(
        fig=fig,
        origen_x=p1[0],
        origen_y=p1[1],
        vx=bx2,
        vy=by2,
        etiqueta="B2",
        color=COLOR_I2
    )

    # Dibujo la distancia entre I2 y P2 >> r2
    dibujar_radio(
        fig=fig,
        origen_x=i2[0],
        origen_y=i2[1],
        destino_x=p1[0],
        destino_y=p1[1],
        etiqueta="r2",
        color=COLOR_I2
    )

    dibujar_componentes_vector(
        fig=fig,
        origen_x=p1[0],
        origen_y=p1[1],
        comp_x=bx2,
        comp_y=by2,
        etiqueta_x="Bx2",
        etiqueta_y="By2",
        color=COLOR_I2
    )

    # Layout
    fig.update_layout(title="Descomposicion vectorial de B2")

    return fig


def visualizacion_resultado_final():
    """
    Objetivo:
        Mostrar el campo magnético total generado por los
        dos conductores sobre el punto P1.

    Retorna:
        go.Figure

    Notas:
        Se muestran únicamente los tres vectores:
            - B1
            - B2
            - BTotal

        No se muestran radios ni componentes para
        obtener una visualización limpia del resultado.
    """


    i1 = (0, 0)
    i2 = (2, 0)
    p1 = (1, 1)
    corriente1 = 1
    corriente2 = 1

    # Cálculo de los campos
    dx1, dy1, r1 = calcular_radio(i1, p1)
    bx1, by1 = componentes_campo(corriente1,r1,dx1,dy1,"entrante")

    dx2, dy2, r2 = calcular_radio(i2, p1)
    bx2, by2 = componentes_campo(corriente2,r2,dx2,dy2,"entrante")

    # Campo total
    bx_total = bx1 + bx2
    by_total = by1 + by2

    # Normalización (solo para dibujar)
    bx1, by1 = normalizar_vector(bx1, by1)
    bx2, by2 = normalizar_vector(bx2, by2)
    bx_total, by_total = normalizar_vector(bx_total,by_total)

    # Escala gráfica
    bx1, by1 = escalar_vector(bx1,by1,0.45)
    bx2, by2 = escalar_vector(bx2,by2,0.45)

    bx_total, by_total = escalar_vector(bx_total,by_total,0.65)

    # Figura base
    fig = visualizacion_base_ejercicio_2()

    # Campo B1
    dibujar_vector(
        fig=fig,
        origen_x=p1[0],
        origen_y=p1[1],
        vx=bx1,
        vy=by1,
        etiqueta="B1",
        color="rgba(220,0,0,0.18)"
    )

    # Campo B2
    dibujar_vector(
        fig=fig,
        origen_x=p1[0],
        origen_y=p1[1],
        vx=bx2,
        vy=by2,
        etiqueta="B2",
        color="rgba(0,0,220,0.20)"
    )

    # Campo total
    dibujar_vector(
        fig=fig,
        origen_x=p1[0],
        origen_y=p1[1],
        vx=bx_total,
        vy=by_total,
        etiqueta="Btotal = B₁ + B₂",
        color="green",
        arrowwidth=4
    )

    # Layout
    fig.update_layout(
        title="Campo Magnético Resultante en P₁"
    )

    return fig