# main.py

from transacoes import buscar_todas_transacoes, buscar_transacoes_ordenadas_por_coluna, gerar_relatorio,ler_arquivo_e_inserir_no_banco
from database import adicionar_transacao, atualizar_transacao, excluir_transacao, apagar_duplicatas, apagar_todos_registros, atualizar_arquivo_txt, transacao_existe

def menu_principal():
    print("\nMenu Principal:")
    print("1. Ver todas as transações")
    print("2. Ver transações ordenadas por coluna")
    print("3. Adicionar nova transação")
    print("4. Atualizar transação existente")
    print("5. Excluir transação")
    print("6. Apagar duplicatas")
    print("7. Apagar todos os registros")
    print("8. Gerar relatório")
    print("9. Atualizar arquivo TXT")
    print("10. Ler transações de um arquivo e inserir no banco")
    print("0. Sair")

def main():
    while True:
        menu_principal()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            buscar_todas_transacoes()
        elif escolha == "2":
            coluna = input("Digite a coluna pela qual deseja ordenar (id, descricao, valor, data): ")
            buscar_transacoes_ordenadas_por_coluna(coluna)
        elif escolha == "3":
            descricao = input("Digite a descrição da transação: ")
            valor = float(input("Digite o valor da transação: "))
            data = input("Digite a data da transação (no formato 'YYYY-MM-DD'): ")
            if not transacao_existe(descricao, valor, data):
                adicionar_transacao(descricao, valor, data)
            else:
                print("Esta transação já existe no banco de dados.")
        elif escolha == "4":
            id_transacao = int(input("Digite o ID da transação que deseja atualizar: "))
            descricao = input("Digite a nova descrição da transação: ")
            valor = float(input("Digite o novo valor da transação: "))
            data = input("Digite a nova data da transação (no formato 'YYYY-MM-DD'): ")
            atualizar_transacao(id_transacao, descricao, valor, data)
        elif escolha == "5":
            id_transacao = int(input("Digite o ID da transação que deseja excluir: "))
            excluir_transacao(id_transacao)
        elif escolha == "6":
            apagar_duplicatas()
        elif escolha == "7":
            apagar_todos_registros()
        elif escolha == "8":
            gerar_relatorio()
        elif escolha == "9":
            caminho_arquivo = 'transacoes.txt'
            atualizar_arquivo_txt(caminho_arquivo)
        elif escolha == "10":
            caminho_arquivo = 'transacoes.txt'
            ler_arquivo_e_inserir_no_banco(caminho_arquivo)
        elif escolha == "0":
            print("Obrigado por usar o sistema de contabilidade. Adeus!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
