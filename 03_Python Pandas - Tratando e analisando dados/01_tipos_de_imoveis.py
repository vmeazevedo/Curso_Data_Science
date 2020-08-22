''' Relatório de Análise II 
Tipos de Imóveis'''

import pandas as pd 

dados = pd.read_csv('dados\\aluguel.csv', sep = ';')

# print(dados.head(10))

# Selecionando somente o que vamos analisar
print(dados['Tipo'])
# print(dados.Tipo)                             # esse método também retornar os nossos valores quando nossa coluna tem um nome valido

# Passando nosso dado para dentro de uma variavel
tipo_de_imovel = dados['Tipo']

# Removendo as duplicadas de nosso dataset na coluna que estamos trabalhando
tipo_de_imovel.drop_duplicates(inplace=True)   # Utilizando o inplace=True para alterar os dados diretamente no metodo
# print(tipo_de_imovel)

''' Organizando a visualização '''
tipo_de_imovel = pd.DataFrame(tipo_de_imovel)
print(tipo_de_imovel)

# Verificando a quantidade de itens
print(tipo_de_imovel.shape[0])

# Apresentando os dados enumerados de forma crescente corretamente
# tipo_de_imovel.index = range(tipo_de_imovel.shape[0])
tipo_de_imovel.index = range(len(tipo_de_imovel))                       # Outra forma de retornar o numero de registros de um DF
tipo_de_imovel.columns.name = 'Id'                                      # Nomeando a coluna do index para Id
print(tipo_de_imovel)                                                   # Apresentando o dataset formatado

