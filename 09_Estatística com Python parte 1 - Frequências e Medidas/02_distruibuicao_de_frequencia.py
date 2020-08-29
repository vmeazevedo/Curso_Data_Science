import pandas as pd

# Importando nossa base e lendo o dataset do projeot
dados = pd.read_csv('data\\dados.csv',sep=',')
print(dados.head())

''' Distribuição de frequências para variáveis qualitativas '''

# Método 2
