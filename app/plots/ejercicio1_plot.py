import plotly.graph_objects as go


def generar_grafico_ejercicio_1():
    # Armo un grafico con valores para ver la curva, porque los valores de r del ejercicio no se aprecian

    distancias = [0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1.0]

    campos = [1e-4,4e-5,2e-5,1e-5,4e-6,2e-6,1e-6,4e-7,2e-7]

    fig = go.Figure()

    # Titulos del grafico
    fig.update_layout(
        title="Campo Magnético vs Distancia → B ∝ 1/r. I es constante",
        xaxis_title="Distancia al conductor (m)",
        yaxis_title="Campo Magnético (T)",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.25,
            xanchor="center",
            x=0.5
        ) # Muevo la leyenda debajo del grafico
    )

    # Agrego leyenda a la derecha del grafico
    fig.add_scatter(
        x=distancias,
        y=campos,
        mode="lines+markers",
        name="B vs r"
    )

    fig.add_scatter(
        x=[1],
        y=[2e-7],
        mode="markers+text",
        text=["1 m → 2×10⁻⁷ T"],
        textposition="top center",
        name="Resultado A"
    )

    fig.add_scatter(
        x=[0.002],
        y=[1e-4],
        mode="markers+text",
        text=["2 mm → 10⁻⁴ T"],
        textposition="top right",
        name="Resultado B"
    )

    # Agrego el conductor en x = 0
    # Reemplazado por el ultimo add_scatter

    # fig.add_vline(
    #     x=0,
    #     line_width=3,
    #     line_dash="dash",
    #     annotation_text="Conductor infinito",
    #     annotation_position="top right"
    # )

    # Agrego una anotacion sobre la curva 
    # Queda muy feo
    # fig.add_annotation(
    #     x=0.05,
    #     y=8e-5,
    #     text=("La distancia r se mide "
    #         "desde el conductor"
    #     ),
    #     showarrow=True
    # )

    # fig.update_xaxes(
    #     range=[-0.05, 1.05]
    # )

    valor_maximo = max(campos) # Uso para agrandar un poco el conductor y que se vea mejor en +x

    # Agrego el conductor en x = 0
    fig.add_scatter(
        x=[0, 0],
        y=[0, valor_maximo * 1.3],
        mode="lines+text",
        name="Conductor rectilíneo  ∞",
        # text=["", "Conductor rectilíneo infinito"],  Quito el texto dentro de la curva
        # textposition="top right",
        line=dict(
            dash="dash",
            width=4
        )
    )

    return fig.to_html(full_html=False)