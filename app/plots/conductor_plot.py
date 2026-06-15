import math

import plotly.graph_objects as go


MU_0 = 4 * math.pi * 1e-7


def generar_grafico_b_vs_i():

    distancia = 1
    corrientes = [0,2,4,6,8,10]
    campos = []

    for corriente in corrientes:
        campo = (MU_0 * corriente) / (2 * math.pi * distancia)
        campos.append(campo)

    fig = go.Figure()

    fig.add_scatter(
        x=corrientes,
        y=campos,
        mode="lines+markers",
        name="B"
    )

    fig.update_layout(
        title="Campo Magnético vs Corriente → B ∝ I",
        xaxis_title="Corriente: I [A]",
        yaxis_title="Campo Magnético: B [μT]"
    )

    fig.add_annotation(
        text="● Valores expresados en μT (microtesla) → [1 μT = 10⁻⁶ T = 0.000001 T]",
        xref="paper",
        yref="paper",
        x=0,
        y=-0.25,
        showarrow=False
    )

    return fig.to_html(full_html=False)


def generar_grafico_b_vs_r():
    corriente = 1
    distancias = [0.05,0.1,0.15,0.2,0.3,0.5,1,2,4,5]
    campos = []

    for distancia in distancias:
        campo = (MU_0 * corriente) / (2 * math.pi * distancia)
        campos.append(campo)

    fig = go.Figure()

    fig.add_scatter(
        x=distancias,
        y=campos,
        mode="lines+markers",
        name="B"
    )

    fig.update_layout(
        title="Campo Magnético vs Distancia → B ∝ 1/r",
        xaxis_title="Distancia: r [m]",
        yaxis_title="Campo Magnético: B [T]"
    )

    return fig.to_html(full_html=False)