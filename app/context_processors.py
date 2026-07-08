from app.services.visitas import contar_visitas


def registrar_context_processors(app):

    @app.context_processor
    def inject_app_data():

        return {
            "visitas": contar_visitas()
        }