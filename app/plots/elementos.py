SENTIDO_ENTRANTE = "entrante"
SENTIDO_SALIENTE = "saliente"


def dibujar_conductor(fig,x,y,sentido,etiqueta,color):
    """
    Dibuja un conductor rectilíneo perpendicular al plano.

    Parámetros
    ----------
    fig : plotly.graph_objects.Figure
        Figura donde se dibuja.

    x, y : float
        Posición del conductor.

    sentido : str
        "entrante" o "saliente".

    etiqueta : str
        Texto identificador (I₁, I₂, etc.).

    color : str
        Color del conductor.
    """

    if sentido == SENTIDO_ENTRANTE:
        simbolo = "⊗"
    else:
        simbolo = "⊙"

    # ------------------------------------------------------
    # Dibujar símbolo
    # ------------------------------------------------------

    fig.add_scatter(
        x=[x],
        y=[y],
        mode="text",
        text=[simbolo],
        textfont=dict(
            size=30,
            color=color
        ),
        showlegend=False,
        hoverinfo="skip"
    )

    # ------------------------------------------------------
    # Dibujar etiqueta
    # ------------------------------------------------------
    fig.add_scatter(
        x=[x],
        y=[y + 0.18],
        mode="text",
        text=[etiqueta],
        textfont=dict(
            size=12,
            color=color
        ),
        showlegend=False,
        hoverinfo="skip"
    )

    def dibujar_punto(fig,x,y,etiqueta,color):
        """ Dibuja un punto del experimento. 
        """

    # ------------------------------------------------------
    # Dibujar marcador
    # ------------------------------------------------------
    fig.add_scatter(
        x=[x],
        y=[y],
        mode="markers",
        marker=dict(
            size=9,
            color=color,
            line=dict(
                color="black",
                width=1
            )
        ),

        showlegend=False,
        hoverinfo="skip"
    )

    # ------------------------------------------------------
    # Dibujar etiqueta
    # ------------------------------------------------------

    fig.add_scatter(
        x=[x],
        y=[y + 0.18],
        mode="text",
        text=[etiqueta],
        textfont=dict(
            size=12,
            color=color
        ),
        showlegend=False,
        hoverinfo="skip"
    )