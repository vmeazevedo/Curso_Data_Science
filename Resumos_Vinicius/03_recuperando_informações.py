import pandas as pd 

dados = pd.read_csv('exemplo_df.csv',sep=';')
print(dados,"\n")

'''Informações Básicas'''
# (linhas, colunas)
d = dados.shape
print(d,"\n")

# Descreve o indice
d = dados.index
print(d,"\n")

# Descreve as colunas
d = dados.columns
print(d,"\n")

# Info sobre o dataframe
d = dados.info()
print(d,"\n")

# Numeros de valores não-NA
d = dados.count()
print(d,"\n")

'''Resumos'''
# Soma de valores
d = dados.População.sum()
print(d,"\n")

# Soma acumulada
d = dados.População.cumsum()
print(d,"\n")

# Valores max e min
d = dados.População.min
d2 = dados.População.max
print(f"O valor minimo é: {d}")
print(f"O valor máximo é: {d2}")

# Sumário estatistico
d = dados.describe()
print(d,"\n")

# Média dos valores
d = dados.mean()
print(d,"\n")

# Mediana dos valores
d = dados.median()
print(d,"\n")


