import pandas as pd

dataset = pd.read_csv('data\\db.csv', sep = ';', index_col = 0)
print(dataset.head())

# Selecionando colunas
print(dataset['Valor'])
print(type(dataset['Valor']))
print(dataset[['Valor']])
print(type(dataset[['Valor']]))

# Selecionando linhas - [i:j]
print(dataset[0:3])

# Utilizando .loc para seleções
'''Seleciona um grupo de linhas e colunas segundo os rótulos ou uma matriz booleana.'''
print(dataset.loc['Passat'])

print(dataset.loc[['Passat', 'DS5']])                       # Imprimindo um dataset com os dados dos dois carros

print(dataset.loc[['Passat', 'DS5'], ['Motor','Valor']])    # Imprimindo um dataset dos dois carros com as informações do motor e valor

print(dataset.loc[:, ['Motor', 'Valor']])                   # Imprimindo as informações de motor e valor de todo o dataset


# Utilizando .iloc para seleções
'''Seleciona com base nos indices, ou seja, se baseia na posição das informações.'''
print(dataset.head())

print(dataset.iloc[[1]])

print(dataset.iloc[1:4])                    # Imprimindo os indices de 1:4

print(dataset.iloc[1:4, [0,5,2]])           # Imprimindo os indices e os valores desejados

print(dataset.iloc[[1, 42, 53], [0,5,2]])   # Imprimindo os indices e valores especificos

print(dataset.iloc[:, [0,5,2]])         # Imprimindo os valores de todos os indices

