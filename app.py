from app import create_app  # Importar la función `create_app`

# Crear la instancia de la aplicación
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)