from flask import Blueprint, render_template, request


conductor_bp = Blueprint(
    "conductor",
    __name__
)

@conductor_bp.route("/conductor",methods=["GET", "POST"])
def conductor():
    corriente = None 
    distancia = None
    
    if request.method == "POST": 
        corriente = request.form.get( "corriente" ) 
        distancia = request.form.get( "distancia" )

    return render_template(
        "conductor.html",
        corriente=corriente,
        distancia=distancia
    )