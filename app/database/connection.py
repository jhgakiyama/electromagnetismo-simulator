import os
import psycopg


def obtener_conexion():
    """
    Devuelve una conexión abierta a PostgreSQL utilizando
    la variable de entorno DATABASE_URL.
    """

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError(
            "La variable de entorno DATABASE_URL no está definida."
        )

    return psycopg.connect(database_url)