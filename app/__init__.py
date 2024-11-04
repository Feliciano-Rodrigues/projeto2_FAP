from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Instância global de SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seu_banco_de_dados.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Conecta SQLAlchemy com a instância de app

    # Registra rotas e blueprints
    from app.routes import agenda_bp
    app.register_blueprint(agenda_bp)

    return app
