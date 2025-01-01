from app import create_app 
from app import db

# Crear y ejecutar la aplicación
app = create_app()
db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)