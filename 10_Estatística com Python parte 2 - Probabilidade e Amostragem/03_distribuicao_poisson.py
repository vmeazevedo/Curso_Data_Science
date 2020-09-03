import pandas as pd 
import numpy as np
from scipy.special import comb
from scipy.stats import binom

# Importando nossa base

dados = pd.read_csv('data\\dados.csv',sep=',')
# print(dados.head())

'''
Problema
Um restaunte recebe em média 20 pedidos por hora. Qual a chance de que, em determinada hora escolhida ao acaso, o restaurante receba 15 pedidos?

Distribuição Poisson
É empregada para descrever o número de ocorrências em um intervalo de tempo ou espaço especifico.
Os eventos são caracterizados pela possibilidade de contagem dos sucesso, mas a não possibilidade de contagem dos fracaddos.
Como exemplos de processo onde podemos aplicar a distribuição de Poisson temos a determinação do número de clientes que entram
em uma loja em determinada hora, o número de crros que chegam em um drive-thru de uma lanchonete na hora do almoço, a determinação
do numero de acidentes registrados em um trecho de estrada, etc.

Onde:
e = constante cujo valor aproximado é 2.718281828459045
u = representa o numero medio de ocorrencias em um determinado intervalo de tempo ou espaço
k = numero de sucessos no intervalo desejado

'''

'''
Experimento Poisson
1 - A probabilidade de uma ocorrencia é a mesma em todo o intervalo observado.
2 - O número de ocorrencia em determinado intervalo é independente do numero de ocorrencias em outros
3 - A probabilidade de uma ocorrencia é a mesma em intervalos de igual comprimento
'''

# Exemplo: Delivery
'''Um restaunte recebe em média 20 pedidos por hora. 
Qual a chance de que, em determinada hora escolhida ao acaso, o restaurante receba 15 pedidos?'''

# Qual o número médio de ocorrências por hora (u)?
media = 20
# Qual o número de ocorrencias que queremos obter no periodo (k)?
k = 15

''' Solução 1 '''
propabilidade = (np.e ** ((-media)) * (media ** k)) / (np.math.factorial(k))
print('%0.8f' % propabilidade)

''' Solução 2 '''
from scipy.stats import poisson
propabilidade = poisson.pmf(k,media)
print('%0.8f' % propabilidade)