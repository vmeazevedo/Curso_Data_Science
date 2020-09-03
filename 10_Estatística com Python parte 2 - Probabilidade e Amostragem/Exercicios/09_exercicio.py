from scipy.stats import norm

'''
O valor do gasto médio dos clientes de uma loja de conveniencia é de R$45,50.
Assumindo que o desvio padrão dos gastos é igual a R$15,00, qual deve ser o
tamanho da amostra para estimarmos a media populacional com um nível de
significancia de 10%?

Considere que o erro maixmo aceitavel seja de 10%.

z = variavel normal padronizada
sigma = desvio padrão populacional
s = desvio padrão amostral
e = erro inferencial
'''

media = 45.5
sigma = 15
significancia = 0.10
confianca = 1 - significancia

# Obtendo o Z
z = norm.ppf(0.5 + (confianca / 2))
print("z =",z)

# Obtendo o sigma
sigma = 15
print("sigma =",sigma)

# Obtendo o (e)
erro_percentual = 0.10
e = media * erro_percentual
print("e =",e)

# Obtendo (n)
n = (z * (sigma / e)) ** 2
print(n)