import pandas as pd 
from scipy.special import comb
from scipy.stats import binom

'''
Um dado, perfeitamente equilibrado, é lançado para o alto dez vezes. 
Utilizando a distribuição binomial, obtenha a probabilidade de o dado 
cair com o número cinco voltado para cima pelo menos três vezes.
'''

# Qual o numero de ensaios (n)?
n = 10
print(f'n é igual = {n}')
# Qual a probabilidade de sucesso (p)?
numero_de_alternativas = 6
p = 1 / numero_de_alternativas
print(f'p é igual = {p}')
# Qual a probabilidade de fracasso (q)?
q = 1 - p
print(f'q é igual = {q}')
# Qual o total de eventos que se deseja obter sucesso (k)?
k = 2
print(f'k é igual = {k}')

dados = binom.sf(k,n,p)
print(f'A probabilidade de cair o numero cinco 3 vezes é de = {dados*100}')