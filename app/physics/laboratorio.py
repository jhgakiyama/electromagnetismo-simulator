from app.physics.tema2 import (
    calcular_radio,
    calcular_campo,
    componentes_campo,
    magnitud_vector
)

from app.plots.tema2_plot import visualizacion_resultado_final


POSICION_I1 = (0.0, 0.0)
POSICION_I2 = (2.0, 0.0)


def obtener_signo_corriente(sentido):
    """
    Convierte el sentido seleccionado por el usuario en el signo físico de la corriente.

    Entrante -> -1
    Saliente -> +1
    """

    if sentido == "entrante":
        return -1

    return 1


def calcular_simulacion(corriente1,sentido1,corriente2,sentido2,px,py):
    """
    Ejecuta una simulación completa del laboratorio del Tema 2.
    """
    configuracion = { 
        "i1": (x1, y1),
        "i2": (x2, y2),
        "p": (px, py)
    }
    
    x1, y1 = POSICION_I1
    x2, y2 = POSICION_I2

    signo_i1 = obtener_signo_corriente(sentido1)
    signo_i2 = obtener_signo_corriente(sentido2)

    i1 = corriente1 * signo_i1
    i2 = corriente2 * signo_i2

    resultado = {}

    return resultado