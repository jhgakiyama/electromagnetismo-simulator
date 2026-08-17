from flask import Blueprint,render_template, request
from app.physics.laboratorio import calcular_simulacion
from app.plots.laboratorio_plot import visualizacion_resultado_laboratorio
from app.services.utils import formatear_resultado_laboratorio


bp = Blueprint(
    "tema2_laboratorio",
    __name__
)

@bp.route("/tema2/laboratorio", methods=["GET", "POST"])
def tema2_laboratorio():
       
    # ==========================================================
    # Estado inicial
    # ==========================================================
    template = "tema2_laboratorio.html"
    resultado = None
    resultado_formateado = None
    grafico = None
    grafico_html = None
    mensaje_error = None

    # ==========================================================
    # Valores por defecto del formulario
    # ==========================================================
    corriente1=1.0
    corriente2=1.0
    sentido1="entrante"
    sentido2="entrante"
    px=1.0
    py=1.0

    if request.method == "POST":
        corriente1 = float(request.form["corriente1"])
        corriente2 = float(request.form["corriente2"])
        sentido1 = request.form["sentido1"]
        sentido2 = request.form["sentido2"]
        px = float(request.form["px"])
        py = float(request.form["py"])
        
        try:
            resultado = calcular_simulacion(
                corriente1=corriente1,
                sentido1=sentido1,
                corriente2=corriente2,
                sentido2=sentido2,
                px=px,
                py=py
            )

            resultado_formateado = formatear_resultado_laboratorio(resultado)
            grafico = visualizacion_resultado_laboratorio(resultado)
            grafico_html = grafico.to_html(
                full_html=False,
                include_plotlyjs="cdn"
            )

        except ValueError as e:

            mensaje_error = str(e) 

    return render_template(
        template,
        resultado=resultado,
        resultado_formateado=resultado_formateado,
        grafico=grafico_html,
        mensaje_error=mensaje_error,
        corriente1=corriente1,
        corriente2=corriente2,
        sentido1=sentido1,
        sentido2=sentido2,
        px=px,
        py=py
    )