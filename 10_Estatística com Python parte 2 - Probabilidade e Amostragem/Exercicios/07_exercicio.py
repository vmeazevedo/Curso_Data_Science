from scipy.stats import norm

'''
O Inmetro verificou que as lâmpadas incandescentes da fabricante XPTO apresentam uma vida 
útil normalmente distribuída, com média igual a 720 dias e desvio padrão igual a 30 dias. 
Calcule a probabilidade de uma lâmpada, escolhida ao acaso, durar:

1) Entre 650 e 750 dias

2) Mais que 800 dias

3) Menos que 700 dias
'''

# Dados
media = 720
desvio_padrao = 30

# 1 - Entre 650 e 750 dias
Z_inferior = (650 - media) / desvio_padrao
Z_superior = (759 - media) / desvio_padrao
probabilidade_1 = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
print("Probabilidade:", probabilidade_1*100)

# 2 - Mais que 800 dias
Z = (800 - media) / desvio_padrao
probabilidade_2 = 1 - norm.cdf(Z)
print("Probabilidade:",probabilidade_2*100)

# 3 - Menos que 700 dias
Z = (700 - media) / desvio_padrao
probabilidade_3 = norm.cdf(Z)
print("Probabilidade:",probabilidade_3*100,"\n")