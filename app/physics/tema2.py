# physics sigue sin saber que existe Plotly.
from math import pi, sqrt

MU0 = 4 * pi * 1e-7

# Responsabilidad de cada funcion:
# magnitud_campo()  → cuánto vale
# vector_perpendicular() → hacia dónde apunta
# componentes_campo() → ¿Cuáles son sus componentes?
# campo_total() → ¿Qué ocurre cuando hay varios conductores? >> ¿Cuál es el campo magnético total en un punto dado?


def magnitud_campo(i, r):
    """
    Objetivo:
        Calcular la magnitud del campo magnético
        producido por un conductor rectilíneo infinito.

    Parámetros:
        i: corriente que circula por el conductor [A]
        r: distancia desde el conductor hasta el punto [m]

    Retorna:
        B: magnitud del campo magnético [T]

    Notas:
        No calcula dirección ni sentido.
        Solamente devuelve la magnitud del campo.
    """

    if r <= 0:
        raise ValueError("La distancia r debe ser mayor que cero.")
    
    return (MU0 * i) / (2 * pi * r)


def vector_perpendicular(x, y, sentido):
    """
    Objetivo:
        Obtener la dirección del campo magnético
        a partir del vector radio.

    Parámetros:
        x: componente X del vector radio
        y: componente Y del vector radio
        sentido: sentido de la corriente
                  ('entrante' o 'saliente')

    Retorna:
        px: componente X del vector perpendicular
        py: componente Y del vector perpendicular

    Notas:
        El vector retornado representa únicamente
        la dirección del campo magnético.

        La magnitud del vector no es relevante
        en esta etapa.
    """

    # ¿Cuál es la dirección?
    if sentido == "entrante":
        return y, -x

    elif sentido == "saliente":
        return -y, x

    raise ValueError(
        "Sentido inválido. Use 'entrante' o 'saliente'."
    )


from math import sqrt


def componentes_campo(i, r, x, y, sentido):
    """
    Objetivo:
        Calcular las componentes cartesianas del
        campo magnético producido por un conductor.

    Parámetros:
        i: corriente que circula por el conductor [A]
        r: distancia al punto de observación [m]
        x: componente X del vector radio
        y: componente Y del vector radio
        sentido: sentido de la corriente
                  ('entrante' o 'saliente')

    Retorna:
        Bx: componente horizontal del campo [T]
        By: componente vertical del campo [T]

    Notas:
        Combina la magnitud del campo con la
        dirección obtenida mediante la regla
        de la mano derecha.
    """

    B = magnitud_campo(i, r)

    px, py = vector_perpendicular(x, y, sentido)

    norma = sqrt(px**2 + py**2)

    ux = px / norma
    uy = py / norma

    Bx = B * ux
    By = B * uy

    return Bx, By


def campo_total(conductores, punto):
    """
    Objetivo:
        Calcular el campo magnético total producido
        por múltiples conductores sobre un punto.

    Parámetros:
        conductores: lista de conductores
        punto: punto de observación

    Retorna:
        Bx: componente horizontal total [T]
        By: componente vertical total [T]
        B: magnitud total del campo [T]

    Notas:
        Realiza la suma vectorial de todas las
        contribuciones individuales.

        Esta función es el punto de entrada
        principal del motor físico del Tema 2.

        Debe funcionar para 2, 3 o más conductores
        sin necesidad de modificar su implementación.
    """

    bx_total = 0.0
    by_total = 0.0

    for conductor in conductores:
        
        dx = punto["x"] - conductor["x"]
        dy = punto["y"] - conductor["y"]

        r = sqrt(dx**2 + dy**2)

        bx, by = componentes_campo(
            i=conductor["i"],
            r=r,
            x=dx,
            y=dy,
            sentido=conductor["sentido"]
        )

        bx_total += bx
        by_total += by

    b_total = sqrt(bx_total**2 + by_total**2)

    return { 
        "bx": bx_total, 
        "by": by_total,
        "b": b_total
    }


def calcular_radio(conductor, punto):
    """
    Objetivo:
        Calcular el vector radio entre un conductor y
        un punto de observación.

    Parámetros:
        conductor:
            Tupla (x, y) con la posición del conductor.

        punto:
            Tupla (x, y) con la posición del punto de
            observación.

    Retorna:
        dx:
            Componente horizontal del vector radio.

        dy:
            Componente vertical del vector radio.

        r:
            Distancia entre el conductor y el punto de
            observación.

    Notas:
        El vector radio siempre se obtiene desde el
        conductor hacia el punto de observación.
    """

    dx = punto[0] - conductor[0]
    dy = punto[1] - conductor[1]

    r = sqrt(dx**2 + dy**2)

    return dx, dy, r


def magnitud_vector(x, y):
    """
    Objetivo:
        Calcular el módulo de un vector a partir de sus
        componentes cartesianas.

    Parámetros:
        x: Componente horizontal.
        y: Componente vertical.

    Retorna: Magnitud del vector.
    """

    return sqrt(x**2 + y**2)