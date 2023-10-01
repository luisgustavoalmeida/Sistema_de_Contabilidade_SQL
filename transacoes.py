# transacoes.py

from database import listar_transacoes, listar_transacoes_ordenadas

# Listar transações ordenadas por data
def buscar_todas_transacoes():
    transacoes = listar_transacoes()
    print("\n\n Transações :")
    for transacao in transacoes:
        print(transacao)


# Listar transações ordenadas por descrição
def buscar_transacoes_ordenadas_por_coluna(variavel_ordem):
     # 'id', 'descricao', 'valor', 'data'
    transacoes_ordenadas_por_descricao = listar_transacoes_ordenadas(variavel_ordem)
    print("\n\n Transações ordenadas por ", variavel_ordem, ":")
    for transacao in transacoes_ordenadas_por_descricao:
        print(transacao)

def somar_valores_transacoes():
    transacoes = listar_transacoes()
    soma = 0
    for transacao in transacoes:
        soma += transacao['valor']
    print(soma)
    return soma



# buscar_transacoes_ordenadas_por_coluna("valor")
# buscar_todas_transacoes()
# somar_valores_transacoes()