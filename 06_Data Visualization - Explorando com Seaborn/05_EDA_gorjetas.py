import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ranksums

''' Analise 4 - Medias '''
gorjetas = pd.read_csv('data\\tips_tratados_4.csv',sep=',')
print(gorjetas.head())

# Pegando a media geral de gorjetas
media_geral_gorjetas = gorjetas.gorjeta.mean().round(3)
print("\n",media_geral_gorjetas)
print(f"A media geral das gorjetas é de {media_geral_gorjetas}")

# Agrupando o dataframe pelo dia da semana e trazendo a media dos valores
print(gorjetas.groupby(['dia_da_semana']).mean().round(3)[['valor_da_conta', 'gorjeta', 'porcentagem']]) 

# Verificando a frequencia de visitação
print("\nFrequência dos dias:\n",gorjetas.dia_da_semana.value_counts())

 
''' Teste de hipótese '''
#Hnull - A distribuição do valor da conta é igual no sabado e no domingo
#Halt - A distribuição do valor da conta não é igual no sabado e no domingo


valor_conta_domingo = gorjetas.query("dia_da_semana == 'Domingo'").valor_da_conta
print(valor_conta_domingo)

valor_conta_sabado = gorjetas.query("dia_da_semana == 'Sabado'").valor_da_conta
print(valor_conta_sabado)

# Teste de Soma de Postos de Wilcoxon-Mann-Whitney
# comparar dois grupos para verificar se eles provém de uma mesma distribuição de probabilidade.
r = ranksums(valor_conta_domingo, valor_conta_sabado)
print(f"\nO valor do p-value é {r.pvalue.round(3)}")

'''
O p-value representa a probabilidade daquela amostra ter acontecido dentro da população. 
Se a chance é pequena, geralmente p-value < 0,05, representa que um evento muito raro aconteceu, 
então optamos por descartar a hipótese nula, e dizer que ela pode não ser verdade.

Porém como o nosso p-value teve um valor alto, iremos aceitar a hipotése null
#Hnull - A distribuição do valor da conta é igual no sabado e no domingo'''