import pandas as pd 
from scipy.special import comb
from scipy.stats import binom

'''
Suponha que a probabilidade de um casal ter filhos com olhos azuis seja de 22%.
Em 50 famílias, com 3 crianças cada uma, quantas podemos esperar que tenham dois filhos com olhos azuis?
'''

# Qual a probabilidade de sucesso (p)?
p= 0.22
# Qual o numero de ensaios (n)?
n = 3
# Qual o total de eventos que se deseja obter sucesso (k)?
k = 2


probabilidade = binom.pmf(k,n,p)
print(f'A probabilidade é de %0.8f' % probabilidade)

# Media de distribuição binomial
filhos = 50 * probabilidade
print(filhos.round(2))