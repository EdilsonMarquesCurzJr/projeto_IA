from flask import Flask
from app import routes

def create_app():
    app = Flask(__name__)

    # Configurações do aplicativo, como a chave secreta
    app.config['SECRET_KEY'] = '123'

    # Importa as rotas
    from app import routes

    return app
