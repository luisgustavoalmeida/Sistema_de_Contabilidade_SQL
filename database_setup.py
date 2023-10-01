# database_setup.py

import mysql.connector

# Conectar ao servidor MySQL (certifique-se de alterar as credenciais conforme necessário)
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
)

cursor = conexao.cursor()

try:
    # Criar o banco de dados se não existir
    cursor.execute("CREATE DATABASE IF NOT EXISTS contabilidade_db")

    # Selecionar o banco de dados criado
    cursor.execute("USE contabilidade_db")

    # Criar a tabela de transações se não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            descricao VARCHAR(255),
            valor DECIMAL(10, 2),
            data DATE
        )
    """)

    print("Banco de dados e tabela criados com sucesso!")
except Exception as e:
    print(f"Erro ao criar o banco de dados e tabela: {e}")
finally:
    cursor.close()  # Fechar o cursor
    conexao.close()  # Fechar a conexão

