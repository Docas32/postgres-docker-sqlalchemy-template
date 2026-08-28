# Local Data Workflow: Postgres (Docker) + SQLAlchemy + Pandas + VS Code

> 🚀 **Workflow prático para desenvolvimento e análise local de dados sem depender do terminal (`psql`).**

Este repositório contém a estrutura completa para subir um banco de dados PostgreSQL isolado via **Docker**, conectar e visualizar tabelas diretamente no **VS Code**, e executar scripts **Python (SQLAlchemy + Pandas)** para criar tabelas, popular dados fictícios e exportar relatórios formatados em `.csv` e `.xlsx`.

---

## 💻 Tecnologias Utilizadas

* **Docker & Docker Compose**: Gerenciamento e isolamento do container PostgreSQL.
* **PostgreSQL (v15-alpine)**: Banco de dados relacional.
* **Python 3.x**: Linguagem base para automação e extração.
* **SQLAlchemy**: ORM / Gerenciador de conexões SQL em Python.
* **Pandas**: Manipulação de dados e exportação de relatórios.
* **VS Code (Extensão SQLTools)**: Interface visual para consultas rápidas no banco.

---

## 📂 Estrutura do Projeto

```text
.
├── docker-compose.yml   # Configuração do container PostgreSQL
├── setup_banco.py       # Script Python para criação da tabela e carga inicial
├── analise_vendas.py    # Script de extração SQL, agregação e geração de relatórios
├── requirements.txt     # Dependências Python do projeto
└── README.md            # Documentação do repositório

```
🚀 Como Executar o Projeto
Pró-requisitos
Docker Desktop instalado e rodando.

Python 3.8+ instalado.

1️⃣ Subir o Container PostgreSQL
Na raiz do projeto, execute o comando para iniciar o banco em segundo plano:
'bash
'docker compose up -d'
O banco estará acessível localmente na porta 5432 com as credenciais padrão definidas no docker-compose.yml:

Host: localhost

Porta: 5432

Usuário: dev_user

Senha: dev_password

Banco: dev_db

2️⃣ Configurar o Ambiente Python
Instale as dependências necessárias:

Bash
pip install -r requirements.txt


Este script irá:

Conectar ao PostgreSQL local via SQLAlchemy.

Ler a tabela vendas e carregar em um DataFrame Pandas.

Exportar os dados brutos para relatorio_vendas.csv.

Agrupar os valores totais por cliente.

Exportar o resumo compilado para resumo_clientes.xlsx.
