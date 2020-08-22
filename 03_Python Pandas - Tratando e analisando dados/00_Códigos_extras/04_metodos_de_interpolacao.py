import pandas as pd 

# Criando uma series para trabalharmos
data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)
print(s)

# Preenchendo os valores com 0
s = s.fillna(0)
print(s)

# Utilizando o ffill para preencher valores null
''' Onde os valores são null ele irá preencher com o ultimo valor válido '''
s = pd.Series(data)
s = s.fillna(method = 'ffill')
print(s)

# Utilizando o bfill para preencher valores null
''' Onde os valores são null ele irá preencher com o valor anterior válido '''
s = pd.Series(data)
s = s.fillna(method = 'bfill')
print(s)

# Utilizando o mean() para preencher valores null com a media dos valores
''' Onde os valores são null ele irá preencher com a media dos valores válidos '''
s = pd.Series(data)
s = s.fillna(s.mean())
print(s)
