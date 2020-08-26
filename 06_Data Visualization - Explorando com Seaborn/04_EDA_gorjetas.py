import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ranksums

''' Analise 3 - Dia da Semana '''
gorjetas = pd.read_csv('data\\tips_tratados_4.csv',sep=',')
print(gorjetas.head())

print(gorjetas.dia_da_semana.unique())

# Apresentando os resultados
# sns.catplot(x='dia_da_semana', y='valor_da_conta', data=gorjetas)
# plt.show()

# sns.relplot(x='valor_da_conta', y='gorjeta',hue='dia_da_semana', data=gorjetas)
# plt.show()

# sns.relplot(x='valor_da_conta', y='gorjeta', hue='dia_da_semana', col='dia_da_semana', data=gorjetas)
# plt.show()

# sns.relplot(x='valor_da_conta', y='porcentagem', hue='dia_da_semana', col='dia_da_semana', data=gorjetas)
# plt.show()

# Plotando a analise de valor x gorjeta x dia da semana
sns.lmplot(x='valor_da_conta', y='gorjeta', hue='dia_da_semana', col='dia_da_semana', data=gorjetas)
plt.show()

# Plotando a analise de valor x percentagem x dia da semana
sns.lmplot(x='valor_da_conta', y='porcentagem', hue='dia_da_semana', col='dia_da_semana', data=gorjetas)
plt.show()

