from flask import Blueprint, render_template

bp = Blueprint(
    "tema3",
    __name__
)

@bp.route("/tema3")
def tema3():

    return render_template(
        "tema3.html",
        titulo="Tema 3 - Bobina Circular"
    )