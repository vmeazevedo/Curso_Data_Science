from scipy.stats import norm

'''
Utilizando a tabela padronizada, ou o ferramental 
disponibilizado pelo Python, encontre a área sob a 
curva normal para os valores de Z abaixo:

1) Z < 1,96

2) Z > 2,15

3) Z < -0,80

4) Z > 0,59
'''

# Z < 1,96
probabilidade_1 = norm.cdf(1.96)
print("Probabilidade:", probabilidade_1)

# Z > 2,15
probabilidade_2 = 1 - norm.cdf(2.15)
print("Probabilidade:", probabilidade_2)

# Z < -0,80
probabilidade_3 = norm.cdf(-0.80)
print("Probabilidade:", probabilidade_3)

# Z > 0,59
probabilidade_4 = 1 - norm.cdf(0.59)
print("Probabilidade:", probabilidade_4)

