# database.py

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='contabilidade_db',
)

cursor = conexao.cursor()


# Função para inserir uma nova transação no banco de dados
def inserir_transacao(descricao, valor, data):
    cursor.execute("INSERT INTO transacoes (descricao, valor, data) VALUES (%s, %s, %s)", (descricao, valor, data))
    conexao.commit()
    cursor.close()
    conexao.close()


# Função para listar todas as transações do banco de dados
# def listar_transacoes():
#     cursor.execute("SELECT * FROM transacoes")
#     return cursor.fetchall()

# Função para listar todas as transações do banco de dados
def listar_transacoes():
    cursor.execute("SELECT * FROM transacoes")
    colunas = [descricao[0] for descricao in cursor.description]
    transacoes = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]
    return transacoes


# Função para listar todas as transações do banco de dados, ordenadas por uma coluna específica
def listar_transacoes_ordenadas(coluna='data'):
    """ Aceita como parametros 'id', 'descricao', 'valor', 'data' """
    colunas_permitidas = ['id', 'descricao', 'valor', 'data']

    if coluna not in colunas_permitidas:
        print("Coluna de ordenação inválida. Usando 'data' como padrão.")
        coluna = 'data'

    query = f"SELECT * FROM transacoes ORDER BY {coluna}"
    cursor.execute(query)
    return cursor.fetchall()


# Função para atualizar uma transação pelo ID no banco de dados
def atualizar_transacao(id, descricao, valor, data):
    cursor.execute("UPDATE transacoes SET descricao = %s, valor = %s, data = %s WHERE id = %s", (descricao, valor, data, id))
    conexao.commit()
    cursor.close()
    conexao.close()


# Função para excluir uma transação pelo ID no banco de dados
def excluir_transacao(id):
    cursor.execute("DELETE FROM transacoes WHERE id = %s", (id,))
    conexao.commit()
    cursor.close()
    conexao.close()

