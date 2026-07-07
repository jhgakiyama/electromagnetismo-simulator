from app.database.connection import obtener_conexion


def crear_tablas():
    # Inicializar el esquema de la base de datos.
    with obtener_conexion() as conn:

        with conn.cursor() as cur:

            cur.execute("""
                CREATE TABLE IF NOT EXISTS visitas (

                    id SERIAL PRIMARY KEY,

                    fecha TIMESTAMP NOT NULL
                        DEFAULT CURRENT_TIMESTAMP

                );
            """)