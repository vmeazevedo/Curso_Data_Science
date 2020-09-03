from scipy.stats import poisson

'''
O número médio de clientes que entram em uma padaria por hora é igual a 20. 
Obtenha a probabilidade de, na próxima hora, entrarem exatamente 25 clientes.
'''

# Qual o número médio de ocorrências por hora (u)?
media = 20
# Qual o número de ocorrencias que queremos obter no periodo (k)?
k = 25

probabilidade = poisson.pmf(k,media)
print('%0.8f' % probabilidade)