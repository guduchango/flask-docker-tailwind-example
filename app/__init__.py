from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
import os
from flask_jwt_extended import JWTManager

# Inicializar SQLAlchemy y Migrate
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    jwt = JWTManager(app)
    app.config.from_object(Config)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://root:rootpassword@localhost:3330/flaskdb"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar rutas
    from .routes.api_routes import bp as api_bp  # Importación de las rutas solo cuando se crea la app
    from .routes.views_routes import bp as views_bp
    app.register_blueprint(api_bp, url_prefix='/api')  # Prefijo para el API
    app.register_blueprint(views_bp)

    return app