from scipy.stats import norm

'''
O faturamento diário de um motorista de aplicativo segue uma distribuição aproximadamente normal, 
com média R$ 300,00 e desvio padrão igual a R$ 50,00. Obtenha as probabilidades de que, em um dia aleatório, o motorista ganhe:

1) Entre R$ 250,00 e R$ 350,00

2) Entre R$ 400,00 e R$ 500,00

'''

# 1
# Indicamos a media
media = 300
# indicamos o desvio padrão
desvio_padrao = 50
# Calculamos o Z
Z_inferior = (250 - media) / desvio_padrao
Z_superior = (350 - media) / desvio_padrao

# Utilizamos o metodo norm para calcular a probabilidade
probabilidade = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
print(probabilidade*100)

# 2
media = 300
desvio_padrao = 50
Z_inferior = (400 - media) / desvio_padrao
Z_superior = (500 - media) / desvio_padrao

probabilidade = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
print(probabilidade*100)

