# ler_arquivo.py

from database import inserir_transacao, transacao_existe
#import os

# Função para ler transações de um arquivo TXT e inserir no banco de dados
def ler_arquivo_txt(caminho_arquivo):
    transacoes = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas[1:]:  # Ignorar a primeira linha (cabeçalho)
                descricao, valor, data = linha.strip().split(',')
                transacoes.append({'descricao': descricao, 'valor': float(valor), 'data': data})
        return transacoes
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []


if __name__ == "__main__":
    caminho_arquivo = 'transacoes.txt'  # Coloque o nome do arquivo se estiver no mesmo diretorio do codigo ou o caminho completo se estiver em outro local

    # Obtém as transações do arquivo
    transacoes = ler_arquivo_txt(caminho_arquivo)

    # Insere as transações no banco de dados
    for transacao in transacoes:
        descricao = transacao['descricao']
        valor = transacao['valor']
        data = transacao['data']
        #inserir_transacao(descricao, valor, data)
        transacao_existe(descricao, valor, data)

    print("Transações carregadas no banco de dados com sucesso!")
