import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ranksums

gorjetas = pd.read_csv('data\\tips_tratados_3.csv',sep=',')

''' Teste de hipótese '''

# Hnull = A distribuição da taxa da gorjeta é a mesma nos dois grupos
# Halt  = A distribuição da taxa da gorjeta não é a mesma nos dois grupos  == pvalue <= 0.05

# Buscando a porcentagem de todo mundo que pediu sobremesa
sobremesa = gorjetas.query("sobremesa == 'Sim'").porcentagem
print(sobremesa.head(3))

# Buscando a porcentagem de todo mundo que não pediu sobremesa
sem_sobremesa = gorjetas.query("sobremesa == 'Não'").porcentagem
print("\n",sem_sobremesa.head(3))

# Teste de Soma de Postos de Wilcoxon-Mann-Whitney
# comparar dois grupos para verificar se eles provém de uma mesma distribuição de probabilidade.
r = ranksums(sobremesa, sem_sobremesa)
print(f"\nO valor do p-value é {r.pvalue.round(3)}")

'''
O p-value representa a probabilidade daquela amostra ter acontecido dentro da população. 
Se a chance é pequena, geralmente p-value < 0,05, representa que um evento muito raro aconteceu, 
então optamos por descartar a hipótese nula, e dizer que ela pode não ser verdade.

Porém como o nosso p-value teve um valor alto, iremos aceitar a hipotése null
Hnull = A distribuição da taxa da gorjeta é a mesma nos dois grupos'''


# Exportando nosso novo DataFrame
gorjetas.to_csv('data\\tips_tratados_4.csv', sep=',', index=False)