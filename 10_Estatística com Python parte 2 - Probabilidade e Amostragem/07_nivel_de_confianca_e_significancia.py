import pandas as pd 
import numpy as np
from scipy.special import comb
from scipy.stats import binom
import matplotlib.pyplot as plt
from scipy.stats import norm

# Importando nossa base
dados = pd.read_csv('data\\dados.csv',sep=',')

'''
Nivel de confiança e significância
O nivel de confiança (1-a) representa a probabilidade de acerto da estimativa. De forma complementar o nivel de significância(a) expressa a probabilidade de erro da 
estimativa.
O nivel de confiança representa o grau de confiabilidade do resultado da estimativa estar dentro de determinado intervalo.
Quando fixamos em uma pesquisa um nível de confiança de 95%, por exemplo, estamos assumindo que existe uma probabilidade de 95% dos resultados da pesquisa representarem
bem a realidade, ou seja, estarem corretos.
O nível de confiança de uma estimativa pode ser obtido a partir da area sob a curva normal.
'''

'''
Intervalo de confiança

Supinha que os pesos dos sacos de arroz de uma industria alimenticia se distribuem aproximadamente como uma normal de desvio padrão populacional igual a 150g.
Selecionada uma amostra aleatoria de 20 sacos de um lote especifico, obteve-se um peso medio de 5.050g. Construa um intervalo de confiança para a media populacional
assumindo um nivel de significância de 5%.
'''

# Media amostral
media_amostral = 5050
print("media amostral =", media_amostral)

# Nivel de significancia(a)
significancia = 0.05
print("significancia =", significancia)

# Nivel de confiança (1-a)
confianca = 1 - significancia
print("confiança =", confianca)

# Obtendo z
z = norm.ppf(0.5 + (0.95 / 2))
print("z =", z)

# Obtendo o sigmax
desvio_padrao = 150

n = 20
raiz_de_n = np.sqrt(n)

sigma = desvio_padrao / raiz_de_n
print("sigma =", sigma)

# Obtendo e
e = z * sigma
print("e =", e)


''' Solução 1 - Calculando o intervalo de confiança para a media '''
intervalo = (
    media_amostral - e,
    media_amostral + e
)
print("intervalo de segurança =", intervalo)

''' Solução 2 - Calculando o intervalo de confiança para a media '''
print(norm.interval(alpha = 0.95, loc = media_amostral, scale = sigma))