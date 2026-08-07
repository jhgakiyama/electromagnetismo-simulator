# Reconfiguración de PostgreSQL en Render

## Esta guia va a permitir crear una nueva BD en Render y continuar trabajando

1. Crear nueva base PostgreSQL.
2. Copiar la nueva DATABASE_URL (url internat).
3. Actualizar la variable de entorno DATABASE_URL del Web Service.
4. La URL Externa la pego en mi .env para hacer los impactos desde mi contenedor local
5. Guardar los cambios (Save Changes).
6. Ejecutar un Manual Deploy.
7. Ejecutar:

   python init_db.py

8. Verificar que la tabla visitas exista.
9. Abrir el sitio y comprobar el contador.