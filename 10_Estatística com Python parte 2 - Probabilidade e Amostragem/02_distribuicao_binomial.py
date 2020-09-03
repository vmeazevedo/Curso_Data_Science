import pandas as pd 
from scipy.special import comb
from scipy.stats import binom

# Importando nossa base

dados = pd.read_csv('data\\dados.csv',sep=',')
# print(dados.head())

'''
Distribuição Binominal 
Exemplo: Gincana
Uma cidade do interior realiza todos os anos uma gincana para arrecadar fundos para o hospital da cidade.
Na ultima gincana se sabe que a proporção de participantes do sexo feminino foi de 60%. O total de equipes,
com 12 integrantes, inscritas na gincana deste ano é de 30. Com as informações acima responda:
Quantas equipes deverão ser formadas por 8 mulheres?
'''
# Qual a probabilidade de sucesso (p)?
p= 0.6
# Qual o numero de ensaios (n)?
n = 12
# Qual o total de eventos que se deseja obter sucesso (k)?
k = 8

probabilidade = binom.pmf(k,n,p)
print(f'A probabilidade é de %0.8f' % probabilidade)

# Media de distribuição binomial
equipes = 30 * probabilidade
print(equipes.round(2))