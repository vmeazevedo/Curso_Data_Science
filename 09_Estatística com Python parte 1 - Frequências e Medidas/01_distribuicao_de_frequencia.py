import pandas as pd

# Importando nossa base e lendo o dataset do projeot
dados = pd.read_csv('data\\dados.csv',sep=',')
print(dados.head())

''' Distribuição de frequências para variáveis qualitativas '''

# Método 1
# Apresentando os dois valores presentes na coluna Sexo
print(dados['Sexo'].value_counts())
# Utilizando o normalize para apresentar o resultado em %
print(dados['Sexo'].value_counts(normalize = True)*100)

frequencia = dados['Sexo'].value_counts()
percentual = dados['Sexo'].value_counts(normalize = True)*100
