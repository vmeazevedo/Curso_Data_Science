''' Relatório de Análise IV
Seleções e Frequências'''

import pandas as pd 
dados = pd.read_csv('dados\\aluguel_residencial.csv', sep=';')
d = dados.head(10)
print(d)

# Selecione somente os imóveis classificados com tipo 'Apartamento'
selecao = dados['Tipo'] == 'Apartamento'
print(selecao)
n1 = dados[selecao].shape[0]
print(n1)

# Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'
selecao = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
print(selecao)
n2 = dados[selecao].shape[0]
print(n2)

# Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites
# Temos que dizer que esta entre, utilizamos a expressão: 60 >= Area <= 100
selecao = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n3 = dados[selecao].shape[0]
print(n3)

# Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 
selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
n4 = dados[selecao].shape[0]
print(n4)

print("Nº de imóveis classificados com tipo 'Apartamento' -> {}".format(n1))
print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila' -> {}".format(n2))
print("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {}".format(n3))
print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {}".format(n4))