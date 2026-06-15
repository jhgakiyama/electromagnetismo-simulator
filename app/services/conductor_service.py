import math

MU_0 = 4 * math.pi * 1e-7

def calcular_campo_magnetico(corriente,distancia):
    campo = (MU_0 * corriente) / (2 * math.pi * distancia)
    return campo

