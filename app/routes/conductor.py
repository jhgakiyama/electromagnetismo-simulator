from flask import Blueprint, render_template, request
from app.services.conductor_service import calcular_campo_magnetico
from app.services.utils import formatear_cientifico
from app.plots.ejercicio1_plot import (generar_grafico_ejercicio_1)
from app.plots.conductor_plot import (
    generar_grafico_b_vs_i,
    generar_grafico_b_vs_r
)

conductor_bp = Blueprint(
    "conductor",
    __name__
)

@conductor_bp.route("/conductor",methods=["GET", "POST"])
def conductor():
    corriente = None 
    distancia = None
    resultado = None
    resultado_formateado = None
    pasos = []
    # Cargo por defecto siempre los 2 graficos
    grafico_b_vs_i = generar_grafico_b_vs_i()
    grafico_b_vs_r = generar_grafico_b_vs_r()
    
    # Cargo el grafico del ejercicio resuelto
    grafico_ejercicio_1 = (generar_grafico_ejercicio_1())


    if request.method == "POST": 
        corriente = float(request.form.get("corriente"))
        distancia = float(request.form.get("distancia"))
        datos_calculo = calcular_campo_magnetico(corriente,distancia)

        resultado = datos_calculo["resultado"]
        pasos = datos_calculo["pasos"]
        resultado_formateado = formatear_cientifico(resultado)

    return render_template(
        "conductor.html",
        corriente=corriente,
        distancia=distancia,
        resultado=resultado,
        resultado_formateado=resultado_formateado,
        pasos=pasos,
        grafico_b_vs_i=grafico_b_vs_i,
        grafico_b_vs_r=grafico_b_vs_r,
        grafico_ejercicio_1=grafico_ejercicio_1
    )



