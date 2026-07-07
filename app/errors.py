from flask import render_template


def register_error_handlers(app):

    @app.errorhandler(404)
    def pagina_no_encontrada(error):
        return render_template("404.html"), 404