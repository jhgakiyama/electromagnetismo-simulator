from flask import Blueprint, render_template, request
from app.services.conductor_service import calcular_campo_magnetico
from app.services.utils import formatear_cientifico


conductor_bp = Blueprint(
    "conductor",
    __name__
)

@conductor_bp.route("/conductor",methods=["GET", "POST"])
def conductor():
    corriente = None 
    distancia = None
    resultado = None
    pasos = []

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
        pasos=pasos
    )



