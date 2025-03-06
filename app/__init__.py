from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializar o SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configurar a URI do banco de dados usando as variáveis do .env
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativar o rastreamento de modificações
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # Chave secreta para sessões

    # Inicializar o banco de dados com a aplicação
    db.init_app(app)

    with app.app_context():
        # Criar as tabelas no banco de dados, se não existirem
        db.create_all()

    return app