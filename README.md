Sistema de Contabilidade
Este é um sistema de contabilidade simples que permite aos usuários gerenciar transações financeiras. O sistema oferece funcionalidades básicas de CRUD (Criar, Ler, Atualizar, Excluir) para transações, além de recursos adicionais como ordenação, remoção de duplicatas e geração de relatórios.

Funcionalidades
Ver todas as transações: Exibe todas as transações armazenadas no banco de dados MySQL local.
Ver transações ordenadas por coluna: Permite ordenar transações com base em colunas como ID, descrição, valor ou data.
Adicionar nova transação: Adiciona uma nova transação ao banco de dados, incluindo descrição, valor e data.
Atualizar transação existente: Permite ao usuário atualizar uma transação existente com novos valores de descrição, valor ou data.
Excluir transação: Remove uma transação específica com base no ID.
Apagar duplicatas: Remove transações duplicadas do banco de dados.
Apagar todos os registros: Remove todas as transações do banco de dados.
Gerar relatório: Gera um relatório das transações, fornecendo uma visão geral dos dados financeiros.
Atualizar arquivo TXT: Atualiza um arquivo TXT externo com as transações do banco de dados.
Como Usar
Requisitos:

Python 3.x
Bibliotecas necessárias: mysql-connector-python
Configuração do Banco de Dados:

Certifique-se de ter um servidor MySQL em execução localmente.
Edite as informações de conexão no arquivo database.py para configurar sua conexão com o banco de dados MySQL local.
Executando o Programa:

Execute main.py para iniciar o sistema.
Escolha uma opção do menu para interagir com o sistema.
Arquivo de Transações:

O sistema suporta a leitura e escrita de transações em um arquivo TXT. Certifique-se de que o arquivo transacoes.txt existe e está no mesmo diretório que os scripts Python.
