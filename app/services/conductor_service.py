import math

MU_0 = 4 * math.pi * 1e-7

def calcular_campo_magnetico(corriente,distancia):
    campo = (MU_0 * corriente) / (2 * math.pi * distancia)
    
    # Muestro los pasos para la proxima seccion
    pasos = [
        "B = μ₀ · I / (2π · r)",
        f"B = ({MU_0:.6e} × {corriente}) / (2π × {distancia})", # puede ser mejor a la vista >> 4π × 10⁻⁷
        f"B = {campo:.6e} T"
    ]
    
    return { 
        "resultado": campo,"pasos": pasos
    }
