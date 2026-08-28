from sqlalchemy import create_engine, text

# 1. Configuração das credenciais do banco
USER = "dev_user"
PASSWORD = "dev_password"
HOST = "localhost"
PORT = "5432"
DB_NAME = "dev_db"

# 2. String de conexão (Database URL)
# Formato: postgresql://USUARIO:SENHA@HOST:PORTA/NOME_DO_BANCO
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# 3. Criando a Engine de conexão
engine = create_engine(DATABASE_URL)

# 4. Script SQL para criar a tabela e inserir registros fictícios
sql_script = """
CREATE TABLE IF NOT EXISTS vendas (
    id SERIAL PRIMARY KEY,
    cliente VARCHAR(100) NOT NULL,
    valor NUMERIC(10, 2) NOT NULL,
    data_venda DATE NOT NULL
);

INSERT INTO vendas (cliente, valor, data_venda) VALUES
    ('Ana Silva', 250.50, '2026-08-01'),
    ('Carlos Eduardo', 1200.00, '2026-08-10'),
    ('Beatriz Lima', 850.00, '2026-08-15'),
    ('Ana Silva', 430.20, '2026-08-20');
"""

try:
    # O engine.begin() abre uma transação, executa o SQL e faz o COMMIT automático
    with engine.begin() as connection:
        connection.execute(text(sql_script))
        print(" Tabela 'vendas' criada e populada com sucesso!")
        
except Exception as e:
    print(f" Ocorreu um erro ao preparar o banco: {e}")