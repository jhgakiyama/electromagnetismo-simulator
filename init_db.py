from app.database.schema import crear_tablas

def main():

    crear_tablas()

    print("Base de datos inicializada correctamente.")

if __name__ == "__main__":
    main()