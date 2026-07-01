from app.physics.tema2 import (
    calcular_radio,
    magnitud_vector,
    magnitud_campo
)

from app.plots.tema2_plot import visualizacion_resultado_final
from app.plots.laboratorio_plot import visualizacion_resultado_laboratorio



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


def componentes_campo_vectorial(corriente,radio,dx,dy):
    """
    Calcula las componentes cartesianas del campo magnético

    Una corriente positiva produce una rotación antihoraria.
    Una corriente negativa produce una rotación horaria.

    Parámetros
    ----------
    corriente : float
        Corriente eléctrica (puede ser positiva o negativa).

    radio : float
        Distancia entre el conductor y el punto.

    dx : float
    dy : float

    Retorna
    -------
    tuple

        (bx, by)
    """

    # Magnitud del campo
    b = magnitud_campo(abs(corriente),radio)

    # Vector radial unitario
    ux = dx / radio
    uy = dy / radio

    # Corriente positiva
    # Giro antihorario
    if corriente >= 0:
        tx = -uy
        ty = ux
    # Corriente negativa
    # Giro horario
    else:
        tx = uy
        ty = -ux

    bx = b * tx
    by = b * ty

    return bx, by



def calcular_simulacion(corriente1,sentido1,corriente2,sentido2,px,py):
    """
    Ejecuta una simulación completa del laboratorio del Tema 2.
    
    Recibe los parámetros del experimento, realiza todos los cálculos necesarios y construye el objeto `resultado`.
    """
    
    
    x1, y1 = POSICION_I1
    x2, y2 = POSICION_I2
    p = (px, py)

    signo_i1 = obtener_signo_corriente(sentido1)
    signo_i2 = obtener_signo_corriente(sentido2)
    i1 = corriente1 * signo_i1
    i2 = corriente2 * signo_i2

    # ==========================================================
    # Campo generado por I1
    # ==========================================================

    dx1, dy1, r1 = calcular_radio(POSICION_I1,p)
    b1 = magnitud_campo(abs(i1),r1)
    bx1, by1 = componentes_campo_vectorial(i1,r1,dx1,dy1)

    # ==========================================================
    # Campo generado por I2
    # ==========================================================

    dx2, dy2, r2 = calcular_radio(POSICION_I2,p)
    b2 = magnitud_campo(abs(i2),r2)
    bx2, by2 = componentes_campo_vectorial(i2,r2,dx2,dy2)

    # ==========================================================
    # ETAPA 4
    # Superposición
    # ==========================================================

    bx = bx1 + bx2
    by = by1 + by2

    btotal = magnitud_vector(bx,by)
    
    fig = visualizacion_resultado_final()

    resultado = {}
    resultado["metadata"] = {"tema": 2,"laboratorio": 1,"version": "1.0"}
    
    resultado["parametros"] = { 
        "corriente1": corriente1,"corriente2": corriente2,
        "corriente1_efectiva": i1,"corriente2_efectiva": i2,
        "sentido1": sentido1,"sentido2": sentido2,
        "px": px,"py": py
    }
    
    resultado["geometria"] = {
        "conductor1": POSICION_I1,
        "conductor2": POSICION_I2,
        "p": p,
        "dx1": dx1,"dy1": dy1,
        "dx2": dx2,"dy2": dy2,
        "r1": r1,"r2": r2
    }

    resultado["b1"] = {"magnitud": b1,"bx": bx1,"by": by1}
    resultado["b2"] = {"magnitud": b2,"bx": bx2,"by": by2}
    resultado["campo_total"] = {"magnitud": btotal,"bx": bx,"by": by}
    
    resultado["grafico"] = visualizacion_resultado_laboratorio(resultado)
    return resultado