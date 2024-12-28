from app import create_app  # Solo importar la función `create_app`

# Crear y ejecutar la aplicación
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)