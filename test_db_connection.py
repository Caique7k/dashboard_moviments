import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a URI do banco de dados
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Criar a URI de conexão
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def test_connection():
    try:
        # Criar um motor de conexão
        engine = create_engine(DATABASE_URL)
        
        # Conectar ao banco de dados
        with engine.connect() as connection:
            print("Conexão com o banco de dados bem-sucedida!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

if __name__ == "__main__":
    test_connection()