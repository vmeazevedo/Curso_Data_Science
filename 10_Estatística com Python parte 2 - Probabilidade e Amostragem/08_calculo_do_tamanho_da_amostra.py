import pandas as pd 
import numpy as np
from scipy.special import comb
from scipy.stats import binom
import matplotlib.pyplot as plt
from scipy.stats import norm

# Importando nossa base
dados = pd.read_csv('data\\dados.csv',sep=',')

'''
Problema
Estamos estudando o rendimento mensal dos chefes de domicilios no Brasil. Nosso supervisor determinou o erro máximo em relação a media seja de R$100,00.
Sabemos que o desvio padrão populacional deste grupo de trabalhadores é de R$3323,39.
Para um nível de confiança de 95%, qual deve ser o tamanho da amostra de nosso estudo?

- Variáveis quantitativas e população infinita
Onde:
z = variavel normal padronizada
sigma = desvio padrão populacional
s = desvio padrão amostral
e = erro inferencial

Observações
1 - O desvio padrão (sigma ou s) e o erro (e) devem estar na mesma unidade de medida.
2 - Quando o erro (e) for representado em termos percentuais, deve ser interpretado como um percentual relacionado a media.
'''

# Obtendo o Z
valor_z = 0.5 + (0.95/2)
Z = norm.ppf(valor_z)
print("Z =",Z)

# Obtendo o sigma
sigma = 3323.39
print("sigma =",sigma)

# Obtendo o (e)
e = 100
print("e =",e)

# Obtendo (n)
n = (Z * (sigma / e)) ** 2
print(n)


'''
Problema
Em um lote de 10.000 lates de refrigerante foi realizada uma amostra aleatoria simples de 100 latas e foi obtido o desvio padrão amostral do conteúdo das latas
igual a 12ml. O fabricante estipula um erro máximo sobre a média populacional de apenas 5ml.
Para garantir um nível de confiança de 95% qual o tamanho de amostra deve ser selecionado para este estudo?

- Variáveis quantitativas e população finita
Onde:
N = tamanho da população
z = variavel normal padronizada
sigma = desvio padrão populacional
s = desvio padrão amostral
e = erro inferencial
'''

# Obtendo N
N = 10000
print("N =",N)

# Obtendo z
z = norm.ppf((0.5 + (0.95/2)))
print("Z =",z)

# Obtendo o s
s =  12
print("s =",s)

# Obtendo o e
e = 5
print("e =",e)

# Obtendo o n
n = ((z**2) * (s**2) * (N)) / (((z**2) * (s**2)) + ((e**2) * (N-1)))
print(n)