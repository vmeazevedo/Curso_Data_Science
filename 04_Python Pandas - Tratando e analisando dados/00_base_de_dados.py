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


''' Informações Gerais sobre a Base de Dados '''
tipo_dados = pd.DataFrame(dados.dtypes, columns= ['Tipos de Dados'])        # Apresentando as informações dos tipos de dados e nomeando a coluna
tipo_dados.columns.name = 'Variáveis'                                       # Renomeando a coluna 0 com o nome de Variaiveis
print(tipo_dados)

dados.shape[0]          # Numero de registros
dados.shape[1]          # Numero de variaveis
print("A base de dados apresenta {} registros (imóveis) e {} variáveis".format(dados.shape[0], dados.shape[1]))

