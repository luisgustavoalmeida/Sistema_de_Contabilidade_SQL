# database.py

import mysql.connector

# Estabelece a conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host='localhost',  # Endereço do servidor do banco de dados
    user='root',  # Nome de usuário do banco de dados
    password='123456',  # Senha do banco de dados
    database='contabilidade_db'  # Nome do banco de dados a ser usado
)

# Cria um objeto de cursor para executar operações no banco de dados
cursor = conexao.cursor()

# Função para inserir uma nova transação no banco de dados
def inserir_transacao(descricao, valor, data):
    '''
    Insere uma nova transação no banco de dados.

    Args:
        descricao (str): Descrição da transação.
        valor (float): Valor da transação.
        data (str): Data da transação no formato 'YYYY-MM-DD'.

    Exemplo de uso:
        inserir_transacao('Compra de mantimentos', 50.0, '2023-11-10')
        # Isso insere uma nova transação no banco de dados com a descrição, valor e data fornecidos.
    '''
    try:
        # Executar a consulta SQL para inserir a transação
        cursor.execute("INSERT INTO transacoes (descricao, valor, data) VALUES (%s, %s, %s)", (descricao, valor, data))

        # Commit para salvar a transação no banco de dados
        conexao.commit()

        # Mensagem de sucesso
        print('Transação inserida com sucesso')
    except Exception as e:
        # Em caso de erro, imprimir a mensagem de erro
        print(f"Erro ao inserir a transação: {e}")


# Função para listar todas as transações do banco de dados
def listar_transacoes():
    '''
    Lista todas as transações do banco de dados.

    Returns:
        list: Uma lista de dicionários representando as transações.

    Exemplo de uso:
        transacoes = listar_transacoes()
        # Isso retorna uma lista de todas as transações no banco de dados.
    '''
    try:
        # Executar a consulta SQL para selecionar todas as transações
        cursor.execute("SELECT * FROM transacoes")

        # Obter os nomes das colunas
        colunas = [descricao[0] for descricao in cursor.description]

        # Construir uma lista de dicionários representando as transações
        transacoes = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]

        # Retornar a lista de transações
        return transacoes
    except Exception as e:
        print(f"Erro ao listar as transações: {e}")


# Função para listar todas as transações do banco de dados, ordenadas por uma coluna específica
def listar_transacoes_ordenadas(coluna='data'):
    '''
    Lista todas as transações do banco de dados, ordenadas por uma coluna específica.

    Args:
        coluna (str): A coluna pela qual as transações devem ser ordenadas. Pode ser 'id', 'descricao', 'valor' ou 'data'.

    Returns:
        list: Uma lista de dicionários representando as transações.

    Exemplo de uso:
        transacoes_ordenadas_por_valor = listar_transacoes_ordenadas('valor')
        # Isso retorna uma lista de transações ordenadas por valor.
    '''
    colunas_permitidas = ['id', 'descricao', 'valor', 'data']

    # Verificar se a coluna de ordenação fornecida é válida, caso contrário, usar 'data' como padrão
    if coluna not in colunas_permitidas:
        print("Coluna de ordenação inválida. Usando 'data' como padrão.")
        coluna = 'data'

    # Construir a consulta SQL para selecionar todas as transações e ordená-las pela coluna especificada
    query = f"SELECT * FROM transacoes ORDER BY {coluna}"

    # Executar a consulta SQL
    cursor.execute(query)

    # Retornar todas as transações ordenadas como uma lista de dicionários
    return cursor.fetchall()


# Função para adicionar uma nova transação ao banco de dados
def adicionar_transacao(descricao, valor, data):
    '''
    Adiciona uma nova transação ao banco de dados.

    Args:
        descricao (str): A descrição da transação.
        valor (float): O valor da transação.
        data (str): A data da transação no formato 'YYYY-MM-DD'.

    Exemplo de uso:
        adicionar_transacao('Nova Despesa', 50.0, '2023-11-10')
        # Isso adiciona uma nova transação com a descrição 'Nova Despesa', valor 50.0 e data '2023-11-10'.
    '''
    try:
        # Executar a consulta SQL para inserir uma nova transação no banco de dados
        cursor.execute("INSERT INTO transacoes (descricao, valor, data) VALUES (%s, %s, %s)", (descricao, valor, data))

        # Confirmar as alterações no banco de dados
        conexao.commit()

        print("Nova transação adicionada com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar a transação: {e}")


# Função para atualizar uma transação pelo ID no banco de dados
def atualizar_transacao(id, descricao, valor, data):
    '''
    Atualiza uma transação no banco de dados com base no ID fornecido.

    Args:
        id (int): O ID da transação que será atualizada.
        descricao (str): A nova descrição para a transação.
        valor (float): O novo valor para a transação.
        data (str): A nova data para a transação no formato 'YYYY-MM-DD'.

    Exemplo de uso:
        atualizar_transacao(5, 'Nova Descrição', 100.50, '2023-10-05')
        # Isso atualiza a transação com o ID 5 com a nova descrição, valor e data.
    '''

    try:
        # Executar a consulta SQL para atualizar a transação com o ID fornecido
        cursor.execute("UPDATE transacoes SET descricao = %s, valor = %s, data = %s WHERE id = %s",
                       (descricao, valor, data, id))

        # Confirmar as alterações no banco de dados
        conexao.commit()
    except Exception as e:
        print(f"Erro ao atualizar a transação: {e}")


# Função para excluir uma transação pelo ID no banco de dados
def excluir_transacao(id):
    '''
    Exclui uma transação do banco de dados com base no ID fornecido.

    Args:
        id (int): O ID da transação que será excluída.

    Exemplo de uso:
        excluir_transacao(5)  # Isso exclui a transação com o ID 5 do banco de dados.
    '''

    try:
        # Executar a consulta SQL para excluir a transação com o ID fornecido
        cursor.execute("DELETE FROM transacoes WHERE id = %s", (id,))

        # Confirmar as alterações no banco de dados
        conexao.commit()
    except Exception as e:
        print(f"Erro ao excluir a transação: {e}")


# Função para apagar duplicatas na tabela 'transacoes' com base em descrição, valor e data
def apagar_duplicatas():
    '''
    Remove duplicatas na tabela 'transacoes' com base na descrição, valor e data.

    A função cria uma tabela temporária para armazenar IDs únicos dos registros não duplicados.
    Em seguida, remove os registros duplicados da tabela 'transacoes' e mantém apenas os registros com IDs únicos.

    Exemplo de uso:
        apagar_duplicatas()
    '''

    try:
        # Criar uma tabela temporária para armazenar IDs únicos
        cursor.execute("""
            CREATE TEMPORARY TABLE tmp_transacoes AS
            SELECT MIN(id) AS id
            FROM transacoes
            GROUP BY descricao, valor, data
        """)

        # Deletar registros que não estão na tabela temporária (ou seja, deletar duplicatas)
        cursor.execute("""
            DELETE FROM transacoes
            WHERE id NOT IN (SELECT id FROM tmp_transacoes)
        """)

        # Remover a tabela temporária após a remoção das duplicatas
        cursor.execute("DROP TEMPORARY TABLE IF EXISTS tmp_transacoes")

        # Confirmar as alterações no banco de dados
        conexao.commit()

        print("Duplicatas removidas com sucesso!")
    except Exception as e:
        print(f"Erro ao remover duplicatas: {e}")


# Função para apagar todos os registros da tabela 'transacoes' e redefinir a contagem do ID para 1
def apagar_todos_registros():
    '''
    Apaga todos os registros da tabela 'transacoes' no banco de dados e redefine a contagem do ID para 1.

    Exemplo de uso:
        apagar_todos_registros()
    '''

    try:
        # Executa o comando SQL para apagar todos os registros da tabela 'transacoes'
        cursor.execute("DELETE FROM transacoes")
        # Redefine a contagem do ID para 1 após apagar os registros
        cursor.execute("ALTER TABLE transacoes AUTO_INCREMENT = 1")
        # Confirma as alterações no banco de dados
        conexao.commit()
        print("Todos os registros apagados com sucesso e contagem de ID resetada!")
    except Exception as e:
        print(f"Erro ao apagar todos os registros: {e}")


# Função para atualizar o arquivo TXT com as transações do banco de dados
def atualizar_arquivo_txt(caminho_arquivo):
    '''
    Atualiza o arquivo de texto com as transações presentes no banco de dados.

    Parâmetros:
        caminho_arquivo (str): Caminho do arquivo TXT a ser atualizado.

    Exemplo de uso:
        caminho_arquivo = 'transacoes.txt'
        atualizar_arquivo_txt(caminho_arquivo)
    '''

    try:
        # Busca no banco de dados apenas as colunas necessárias para atualizar o arquivo
        cursor.execute("SELECT descricao, valor, data FROM transacoes")
        transacoes = cursor.fetchall()
        print("As transações presentes no site são:\n\n")
        print(transacoes)

        try:
            # Abre o arquivo em modo de escrita
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                # Escreve o cabeçalho no arquivo
                arquivo.write("descricao,valor,data\n")
                # Escreve as transações no arquivo
                for transacao in transacoes:
                    descricao, valor, data = transacao
                    arquivo.write(f"{descricao},{valor},{data}\n")
            print("Arquivo atualizado com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar o arquivo: {e}")

    except Exception as e:
        print(f"Erro ao buscar transações do banco de dados: {e}")
        return []


# Função para verificar se uma transação já existe no banco de dados
def transacao_existe(descricao, valor, data):
    '''
    Verifica se uma transação com a mesma descrição, valor e data já existe no banco de dados.

    Args:
        descricao (str): Descrição da transação.
        valor (float): Valor da transação.
        data (str): Data da transação no formato 'YYYY-MM-DD'.

    Returns:
        bool: Retorna True se a transação existe, False caso contrário.

    Exemplo de uso:
        existe = transacao_existe('Compra de mantimentos', 50.0, '2023-11-10')
        # Isso verifica se uma transação com a descrição, valor e data fornecidos já existe no banco de dados.
        # A variável 'existe' será True se a transação existir e False caso contrário.
    '''
    try:
        # Executa uma consulta SQL para contar o número de transações com os mesmos detalhes
        cursor.execute("SELECT COUNT(*) FROM transacoes WHERE descricao = %s AND valor = %s AND data = %s",
                       (descricao, valor, data))
        count = cursor.fetchone()[0]  # Obtém o resultado da consulta (número de transações encontradas)
        return count > 0  # Retorna True se existirem transações com os mesmos detalhes, caso contrário, retorna False
    except Exception as e:
        # Em caso de erro, imprimir a mensagem de erro
        print(f"Erro ao verificar a existência da transação: {e}")
        return False  # Retorna False em caso de erro durante a execução da consulta SQL




