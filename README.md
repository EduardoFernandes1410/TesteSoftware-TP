# TesteSoftware-TP
TP de Teste de Software - DCC - UFMG

## Membros do Grupo
- Augusto Maillo Queiroga de Figueiredo - 2019006450
- Eduardo Augusto Militão Fernandes - 2019006540
- Pedro Dias Pires - 2019007040
- Arthur de Brito Bonifácio - 2019006370

## Explicação do Sistema
Neste trabalho, desenvolvemos um sistema de gerenciamento de comércio por linha de comando. Este sistema possui 3 modos de operação disponíveis: modo caixa, modo gerente e modo de relatório. Cada um deles será detalhado a seguir:

### Modo Caixa
Neste modo de operação, o usuário do sistema pode abrir uma nova compra e, então, adicionar os produtos sendo comprados junto de suas quantidades, remover produtos adicionados, fechar a compra, validando-a no sistema (verificando se as quantidades adicionadas estão disponíveis no inventório) e, então, registrar a compra no sistema, atualizando as quantidades no inventório e armazenando a compra no banco de dados.

### Modo Gerente
No modo gerente, o usuário tem a capacidade de cadastrar produtos novos no inventório do comércio, informando o nome, preço e quantidade disponível do produto, atualizar o preço de algum produto, remover um produto do sistema e alterar o estoque de um produto, informando tanto uma quantidade positiva (recarregamento de estoque) quanto negativa (perda de estoque) de variação.

### Modo Relatório
Neste modo, o usuário pode gerar diversos relatórios sobre todos os dados do sistema, a fim de consultar informações sobre o seu uso e de seus clientes. Alguns dos relatórios disponíveis para serem gerados são: exibir todas as comprar realizadas em determinado período, exibir os itens mais vendidos, exibir os itens mais lucrativos, exibir os dias com mais volume de vendas, etc.

## Tecnologias Utilizadas
- Linguagem de programação: Python3
- Framework de teste: unittest
- Banco de dados: Pandas
- Automatização dos testes: GitHub Actions
