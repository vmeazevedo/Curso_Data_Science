''' Relatório de Análise I
Importando a Base de Dados'''

import pandas as pd

dados = (pd.read_csv('dados\\aluguel.csv', sep = ';'))
# print(dados)

# Tipo da variavel criada
print(type(dados))

# Informações do DataFrame
print(dados.info())

# Apresentando os 10 primeiros itens dos nossos dados
print(dados.head(10))

