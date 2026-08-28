import pandas as pd
from sqlalchemy import create_engine

# 1. Conexão com o banco local
DATABASE_URL = "postgresql://dev_user:dev_password@localhost:5432/dev_db"
engine = create_engine(DATABASE_URL)

# 2. Query de extração
query_vendas = """
    SELECT 
        id, 
        cliente, 
        valor, 
        data_venda 
    FROM vendas 
    ORDER BY data_venda DESC;
"""

print(" Extraindo dados do PostgreSQL...")

# 3. Lendo a query e carregando direto em um DataFrame do Pandas
df_vendas = pd.read_sql_query(query_vendas, con=engine)

# Exibindo o resultado formatado no console
print("\n--- Primeiras Linhas do DataFrame ---")
print(df_vendas)

# 4. Exportando a tabela completa para CSV
df_vendas.to_csv("relatorio_vendas.csv", index=False)
print("\n Arquivo 'relatorio_vendas.csv' gerado com sucesso!")

# 5. Agregação com Pandas: Soma total de vendas por cliente
resumo_clientes = df_vendas.groupby("cliente")["valor"].sum().reset_index()
resumo_clientes.rename(columns={"valor": "total_gasto"}, inplace=True)

print("\n--- Resumo por Cliente ---")
print(resumo_clientes)

# 6. Exportando o resumo para Excel
resumo_clientes.to_excel("resumo_clientes.xlsx", index=False)
print("\n Relatório 'resumo_clientes.xlsx' gerado com sucesso!")