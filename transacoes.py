# transacoes.py

from database import listar_transacoes, listar_transacoes_ordenadas, adicionar_transacao, inserir_transacao,transacao_existe
import statistics


# Função para buscar e imprimir todas as transações
def buscar_todas_transacoes():
    # Obtém a lista de transações do banco de dados
    transacoes = listar_transacoes()

    # Imprime as transações
    print("\n\n Transações ordenadas por data:")
    for transacao in transacoes:
        print(transacao)


# Listar transações ordenadas por descrição
def buscar_transacoes_ordenadas_por_coluna(variavel_ordem):
    #  'id', 'descricao', 'valor', 'data'
    transacoes_ordenadas_por_descricao = listar_transacoes_ordenadas(variavel_ordem)
    print("\n\n Transações ordenadas por ", variavel_ordem, ":")
    for transacao in transacoes_ordenadas_por_descricao:
        print(transacao)


def gerar_relatorio():
    # Obter todas as transações do banco de dados
    transacoes = listar_transacoes()

    # Separar descrições, datas e valores das transações
    descricoes = [transacao['descricao'] for transacao in transacoes]
    datas = [transacao['data'] for transacao in transacoes]
    valores = [transacao['valor'] for transacao in transacoes]

    # Separar as transações em despesas (valores negativos) e salários (valores positivos)
    despesas = [{'valor': valor, 'descricao': desc, 'data': data} for valor, desc, data in
                zip(valores, descricoes, datas) if valor < 0]
    salarios = [{'valor': valor, 'descricao': desc, 'data': data} for valor, desc, data in
                zip(valores, descricoes, datas) if valor > 0]

    # Calcular estatísticas básicas para despesas
    if despesas:
        # Encontrar a maior e menor despesa usando a função min e max com uma lambda function
        maior_despesa = min(despesas, key=lambda x: x['valor'])
        menor_despesa = max(despesas, key=lambda x: x['valor'])
        # Calcular a média e o desvio padrão das despesas usando a biblioteca statistics
        media_despesa = statistics.mean([despesa['valor'] for despesa in despesas])
        desvio_padrao_despesa = statistics.stdev([despesa['valor'] for despesa in despesas])
    else:
        # Se não houver despesas, definir valores padrão para maior, menor e média
        maior_despesa = {'valor': 0, 'descricao': '', 'data': ''}
        menor_despesa = {'valor': 0, 'descricao': '', 'data': ''}
        media_despesa = 0

    # Calcular estatísticas básicas para salários
    if salarios:
        # Encontrar a maior e menor salário usando a função min e max com uma lambda function
        maior_salario = max(salarios, key=lambda x: x['valor'])
        menor_salario = min(salarios, key=lambda x: x['valor'])
        # Calcular a média dos salários usando a biblioteca statistics
        media_salario = statistics.mean([salario['valor'] for salario in salarios])
    else:
        # Se não houver salários, definir valores padrão para maior, menor e média
        maior_salario = {'valor': 0, 'descricao': '', 'data': ''}
        menor_salario = {'valor': 0, 'descricao': '', 'data': ''}
        media_salario = 0

    # Imprimir o relatório
    print("Despesas:")
    print(f"Maior Despesa: {maior_despesa['valor']} (Descrição: {maior_despesa['descricao']}, Data: {maior_despesa['data']})")
    print(f"Menor Despesa: {menor_despesa['valor']} (Descrição: {menor_despesa['descricao']}, Data: {menor_despesa['data']})")
    print(f"Média de Despesas: {media_despesa}")
    print(f"Desvio Padrão das Despesas: {desvio_padrao_despesa}")

    print("\nSalários:")
    print(f"Maior Salário: {maior_salario['valor']} (Descrição: {maior_salario['descricao']}, Data: {maior_salario['data']})")
    print(f"Menor Salário: {menor_salario['valor']} (Descrição: {menor_salario['descricao']}, Data: {menor_salario['data']})")
    print(f"Média de Salários: {media_salario}")

    # Você pode adicionar outras estatísticas conforme necessário
    return {
        'maior_despesa': maior_despesa['valor'],
        'descricao_maior_despesa': maior_despesa['descricao'],
        'data_maior_despesa': maior_despesa['data'],
        'menor_despesa': menor_despesa['valor'],
        'descricao_menor_despesa': menor_despesa['descricao'],
        'data_menor_despesa': menor_despesa['data'],
        'media_despesa': media_despesa,
        'desvio_padrao_despesa': desvio_padrao_despesa,
        'maior_salario': maior_salario['valor'],
        'descricao_maior_salario': maior_salario['descricao'],
        'data_maior_salario': maior_salario['data'],
        'menor_salario': menor_salario['valor'],
        'descricao_menor_salario': menor_salario['descricao'],
        'data_menor_salario': menor_salario['data'],
        'media_salario': media_salario
        # Adicione outras estatísticas ao dicionário conforme necessário
    }


# Função para ler transações de um arquivo TXT e retornar uma lista de dicionários
def ler_arquivo_txt(caminho_arquivo):
    transacoes = []  # Lista para armazenar as transações lidas do arquivo
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas[1:]:  # Começa a ler a partir da segunda linha para ignorar o cabeçalho
                descricao, valor, data = linha.strip().split(',')  # Divide a linha em descrição, valor e data
                transacoes.append({'descricao': descricao, 'valor': float(valor), 'data': data})  # Adiciona a transação à lista como um dicionário
        return transacoes  # Retorna a lista de transações
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
        return []  # Retorna uma lista vazia se o arquivo não for encontrado
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []  # Retorna uma lista vazia se ocorrer algum erro durante a leitura do arquivo


# Função para ler transações de um arquivo e inserir no banco de dados
def ler_arquivo_e_inserir_no_banco(caminho_arquivo):
    # Obtém as transações do arquivo usando a função ler_arquivo_txt
    transacoes = ler_arquivo_txt(caminho_arquivo)

    # Insere as transações no banco de dados apenas se não existirem no banco
    for transacao in transacoes:
        descricao = transacao['descricao']
        valor = transacao['valor']
        data = transacao['data']

        # Verifica se a transação já existe no banco de dados usando a função transacao_existe
        if not transacao_existe(descricao, valor, data):
            inserir_transacao(descricao, valor, data)  # Insere a transação no banco de dados usando a função inserir_transacao
            print(f"Transação inserida: {descricao}, {valor}, {data}")
        else:
            print(f"Transação já existe no banco de dados: {descricao}, {valor}, {data}")

    print("Processo de carga concluído.")  # Mensagem indicando que o processo de carga foi concluído


# caminho_arquivo = 'transacoes.txt' # Coloque o nome do arquivo se estiver no mesmo diretório do código ou o caminho completo se estiver em outro local
# # #
# ler_arquivo_e_inserir_no_banco(caminho_arquivo)


#gerar_relatorio()

