import pandas as pd 
import numpy as np
from scipy.special import comb
from scipy.stats import binom
from scipy.stats import norm

# Importando nossa base

dados = pd.read_csv('data\\dados.csv',sep=',')
# print(dados.head())

'''
Distribuição Normal
A distribuição normal é uma das mais utilizadas em estatistica. É uma distribuição continnua, onde a distribuição de frenquencias de 
uma variavel quantitativa apresenta a forma de sino e é simetrica em relação a sua média.'''

'''
Caracteristicas importantes:

1 - É simetrica em torno da media;
2 - A area sob a curva corresponde a proporção 1 ou 100%¨;
3 - As medidas de tendencia central (media, mediana e moda) apresentam o mesmo valor;
4 - Os extremos da curva tendem ao infinito em ambas as direções e, teoricamente, jamais tocam o eixo x;
5 - O desvio padrão define o achatamento e largura da distribuição. Curvas mais largas e mais achatadas apresentam valores maiores de desvio padrão;
6 - A distribuição é definida por sua média e desvio padrão;
7 - A probabilidade sempre será igual a area sob a curva, delimitada pelos limites inferiores e superiores.

Onde:
x = variavel nominal
sigma = desvio padrão
u = media
'''

''' 
Tabelas padronizadas
As tabelas padronizadas foram criadas para facilitar a obtenção dos valores das areas sob a curva normal e eliminar a necessidade de solucionar integrais definidas.
Para consultarmos os valores em uma tabela padronizada basta transformarmos nossa variavel em uma variavel padronizada Z.
Esta variavel Z representa o afastamento em desvios padrões de um valor variavel original em relação a media.

Onde:
x = variavel normal com a media u e desvio padrão sigma
sigma = desvio padrão
u = media
'''

import pandas as pd 
import numpy as np
from scipy.stats import norm

tabela_normal_padronizada = pd.DataFrame(
    [],
    index=["{0:0.2f}".format(i / 100) for i in range(0,400,10)],
    columns=["{0:0.2f}".format(i / 100) for i in range(0,10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)
print("Tabelas Padronizadas")
print(tabela_normal_padronizada,"\n")

'''
Exemplo: Qual a sua altura?
Problema
Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue uma distribuição aproximadamente
normal, com média 1.70 e desvio padrão de 0.1. Com estas informações obtenha o seguinte conjunto de probabilidades:

A - probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1.80 metros
B - probabilidade de uma pessoa, selecionada ao acaso, ter entre 1.60 e 1.80 metros
C - probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1.90 metros.
'''

'''Problema A - Identificação da area sob a curva'''
# Obter a variavel padronizada Z
media = 1.7 
desvio_padrao = 0.1
Z = (1.8 - media) / desvio_padrao
print(f'Z = {Z}')


''' Solução 1 - Utilizando a tabela '''
# Quando temos o valor de Z procuramos a porcentagem diretamente em nossa tabela
probabilidade = 0.8413

''' Solução 2 - Utilizando o Scipy '''
from scipy.stats import norm
print("Probabilidade:",norm.cdf(Z),"\n")


'''Problema B - Identificação da area sob a curva'''
# Obter a variavel padronizada Z
Z_superior = (1.8 - media) / desvio_padrao
print(f'Z = {Z}')

''' Solução 1 - Utilizando a tabela '''
# Quando temos o valor de Z procuramos a porcentagem diretamente em nossa tabela
probabilidade = (0.8413 - 0.5) * 2 

''' Solução 2 - Utilizando o Scipy '''
probabilidade = norm.cdf(Z_superior) - (1 - norm.cdf(Z_superior))
print("Probabilidade:",probabilidade,"\n")


'''Problema C - Identificação da area sob a curva'''
# Obter a variavel padronizada Z
Z = (1.9 - media) / desvio_padrao
print(f'Z = {Z}')

''' Solução 1 - Utilizando a tabela '''
# Quando temos o valor de Z procuramos a porcentagem diretamente em nossa tabela
probabilidade = 1 - 0.9767

''' Solução 2 - Utilizando o Scipy '''
probabilidade = 1 - norm.cdf(Z)
print("Probabilidade:",probabilidade,"\n")