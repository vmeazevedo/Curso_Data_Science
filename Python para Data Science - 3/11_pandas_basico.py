import pandas as pd

# Series
'''Series são arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dados.
Os rotulos das linhas são chamados de index. A forma básica de criação de uma serie é a seguinte:

s = pd.Series(dados, index = index)'''

# DataFrames
'''DataFrame é uma estrutura de dados tabular bidimensional com rotulos nas linhas e colunas. 
Como a Series, os DataFrames são capazes de armazenar qualquer tipo de dados.

df = pd.DataFrame(dados, index = index, columns = columns)
'''

# Estruturas de dados
# Criando uma Serie a partir de uma lista
carros = ['Jetta Variant', 'Passat', 'Crossfox']
s = pd.Series(carros)
print(s)


# Criando um DataFrame a partir de uma lista de dicionarios
dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_Km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_Km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_Km': False, 'Valor': 72832.16}
]

dataset = pd.DataFrame(dados)
print(dataset)

# Imprimindo o DataFrame na ordem desejada
print(dataset[['Nome', 'Ano', 'Motor', 'Valor', 'Quilometragem', 'Zero_Km']])

