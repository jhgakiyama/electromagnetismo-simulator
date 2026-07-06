from flask import Blueprint, jsonify

health_bp = Blueprint(
    "health",
    __name__
)

@health_bp.route("/healthz")
def health_check():
    return jsonify(
        {
            "status": "ok",
            "service": "Laboratorio Virtual de Electromagnetismo",
            "version": "0.6.0"
        }
    ), 200