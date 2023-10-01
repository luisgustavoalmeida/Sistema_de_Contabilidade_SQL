# pip install mysql-connector-python

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='bdaula',
)

cursor = conexao.cursor()

# CRUD

# # CREATE
#
# nome_produto = "todynho"
# valor = 5
# comando = f'INSERT INTO vendas(nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados
# cursor.close()
# conexao.close()

# # READ
#
# comando = f'SELECT * FROM vendas;'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados e retorna uma lista de tuplas
# print(resultado)
# cursor.close()
# conexao.close()

# # UPDATA
#
# nome_produto = "todynho"
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados
# cursor.close()
# conexao.close()

# # DELETE
#
# nome_produto = "todynho"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados
#
# cursor.close()
# conexao.close()



