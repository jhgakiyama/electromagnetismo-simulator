from flask import Blueprint, render_template

conductor_bp = Blueprint(
    "conductor",
    __name__
)

@conductor_bp.route("/conductor")
def conductor():

    return render_template(
        "conductor.html"
    )