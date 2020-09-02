import pandas as pd 
from scipy.special import comb
from scipy.stats import binom

'''
Uma moeda, perfeitamente equilibrada, é lançada para o alto quatro vezes. 
Utilizando a distribuição binomial, obtenha a probabilidade de a moeda cair
com a face coroa voltada para cima duas vezes.
'''

# Qual o numero de ensaios (n)?
n = 4
print(f'n é igual = {n}')
# Qual a probabilidade de sucesso (p)?
numero_de_alternativas = 2
p = 1 / numero_de_alternativas
print(f'p é igual = {p}')
# Qual a probabilidade de fracasso (q)?
q = 1 - p
print(f'q é igual = {q}')
# Qual o total de eventos que se deseja obter sucesso (k)?
k = 2
print(f'k é igual = {k}')

coroa = binom.pmf(k,n,p)
print(f'A probabilidade de dar coroa duas vezes é de = {coroa}')