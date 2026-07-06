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
    
    if r1 == 0:
        raise ValueError(
            "El punto de observación coincide con el conductor I1."
        )

    if r2 == 0:
        raise ValueError(
            "El punto de observación coincide con el conductor I2."
        )