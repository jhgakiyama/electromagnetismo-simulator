EPSILON = 1e-9


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
        )

    if r2 < EPSILON :
        raise ValueError(
            "El punto de observación coincide con el conductor I2."
        )