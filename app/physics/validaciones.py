EPSILON = 1e-9

# ==========================================================
# Límites del laboratorio (cm)
# ==========================================================

LIMITE_COORDENADA = 20


def validar_geometria_experimento(r1, r2):
    """
    Valida la geometría del experimento antes
    de realizar los cálculos físicos.
    
    Lanza
    -----
    ValueError
        Si el punto de observación coincide
        con alguno de los conductores.
    """
    
    if r1 < EPSILON :
        raise ValueError(
            "El punto de observación coincide con el conductor I1."
            "En esa posición el modelo del conductor rectilíneo infinito presenta una singularidad (r = 0), por lo que no es posible calcular el campo magnético."
            
        )

    if r2 < EPSILON :
        raise ValueError(
            "El punto de observación coincide con el conductor I2."
            "En esa posición el modelo del conductor rectilíneo infinito presenta una singularidad (r = 0), por lo que no es posible calcular el campo magnético."
        )
    

def validar_corrientes(corriente1,corriente2):
    """
    Valida que las corrientes del experimento sean físicamente válidas.

    Lanza
    ------
    ValueError
        Si alguna corriente es menor o igual a cero.
    """

    if corriente1 <= 0:
        raise ValueError(
            "La corriente del conductor I₁ debe ser mayor que cero."
        )

    if corriente2 <= 0:
        raise ValueError(
            "La corriente del conductor I₂ debe ser mayor que cero."
        )
    

def validar_limites_laboratorio(px,py):
    """
    Valida que el punto de observación se encuentre
    dentro del área de trabajo del laboratorio.

    Lanza
    ------
    ValueError
        Si el punto está fuera de los límites permitidos.
    """

    if not (-LIMITE_COORDENADA <= px <= LIMITE_COORDENADA):
        raise ValueError(
            f"La coordenada X debe estar entre "
            f"-{LIMITE_COORDENADA} cm y {LIMITE_COORDENADA} cm."
        )

    if not (-LIMITE_COORDENADA <= py <= LIMITE_COORDENADA):
        raise ValueError(
            f"La coordenada Y debe estar entre "
            f"-{LIMITE_COORDENADA} cm y {LIMITE_COORDENADA} cm."
        )