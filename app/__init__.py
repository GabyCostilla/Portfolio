# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    # Importa las rutas aquí para evitar la referencia circular
    with app.app_context():
        from . import index  # Importa el archivo index.py aquí, que contiene las rutas
        db.create_all()

    return app
