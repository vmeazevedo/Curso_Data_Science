import pandas as pd 
import numpy as np
from scipy.special import comb
from scipy.stats import binom

import matplotlib.pyplot as plt

# Importando nossa base
dados = pd.read_csv('data\\dados.csv',sep=',')


'''
- Problema

Suponha que os pesos dos sacos de arroz de uma industria alimenticia se distribuem aproximadamente como uma normal de desvio padrão populacional igual a 150g.
Selecionada uma amostra aleatorio de 20 sacos de um lote especifico, obteve-se um peso medio de 5.050g. Construa um intervalo de confiança para a media populacional
assumindo um nivel de significancia de 5%.
'''

'''
Estimação
É a forma de se fazer suposições generalizadas sobre os parametros de uma população tendo como base informações de uma amostra.
- Parametros são atributos numericos de uma população, tal como a media, desvio padrão, etc
- Estimativa é o valor obtido para determinado parametro a partir dos dados de uma amostra da população.

Teorema do limite central
O teorema do limite central afirma que, com o aumento do tamanho da amostra, a distribuição das médias amostrais se aproxima de uma distribuição normal com media
igual a media da população e desvio padrão igual ao desvio padrão da variavel original pela raiz quadrada do tamanho da amostra. Este fato é assegurado para n maior
ou igual a 30.

O desvio padrão das medias amostrais é conhecido como erro padrão da média.
'''

# Entendendo o Teorema do Limite Central
n = 2000
total_de_amostras = 1500
amostras = pd.DataFrame()

for i in range(total_de_amostras):
    _ = dados.Idade.sample(n)
    _.index = range(0, len(_))
    amostras['Amostra_' + str(i)] = _

# print(amostras)

# com o aumento do tamanho da amostra, a distribuição das médias amostrais se aproxima de uma distribuição normal
amostras.mean().hist()
# plt.show()

# com media igual a media da população
print(dados.Idade.mean())
print(amostras.mean().mean())

# desvio padrão igual ao desvio padrão da variavel original pela raiz quadrada do tamanho da amostra
print(amostras.mean().std())

