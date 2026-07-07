from app.database.connection import obtener_conexion


SQL_INSERT_VISITA = """
INSERT INTO visitas
DEFAULT VALUES;
"""


SQL_CONTAR_VISITAS = """
SELECT COUNT(*)
FROM visitas;
"""


def registrar_visita() -> None:
    """
    Registra una nueva visita en la base de datos.
    """

    with obtener_conexion() as conn:

        with conn.cursor() as cur:

            cur.execute(SQL_INSERT_VISITA)


def contar_visitas() -> int:
    """
    Devuelve la cantidad total de visitas registradas.
    """

    with obtener_conexion() as conn:

        with conn.cursor() as cur:

            cur.execute(SQL_CONTAR_VISITAS)

            cantidad = cur.fetchone()[0]

            return cantidad