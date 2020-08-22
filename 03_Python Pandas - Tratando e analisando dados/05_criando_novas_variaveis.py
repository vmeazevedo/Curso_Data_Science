''' Relatório de Análise VI
Criando Novas Variáveis '''

import pandas as pd 

dados = pd.read_csv('dados\\aluguel_residencial_2.csv', sep=';')
h = dados.head(10)
print(h,"\n")

# Criando uma nova variavel de Valor Bruto, contendo o valor de valor + condiminio + iptu
dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']
h = dados.head(10)
print(h,"\n")

# Criando o valor do m² em uma nova coluna
dados['Valor m2'] = (dados['Valor'] / dados['Area']).round(2)       # Calculando o valor m² e arrendondando ele
h = dados.head(10)
print(h,"\n")

# Criando o valor bruto do m² em uma nova coluna
dados['Valor Bruto m2'] = (dados['Valor Bruto'] / dados['Area']).round(2)       # Calculando o valor m² e arrendondando ele
h = dados.head(10)
print(h,"\n")

# Identificando os tipos e reclassificando eles no tipo agregado
casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')    # .apply permite aplicarmos uma função para cada registro do nosso DF
d = dados.head(10)
print(d,"\n")
