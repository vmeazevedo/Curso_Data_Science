import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

'''
Dados:
data - Data
temp_media - Temperatura Média (°C)
temp_min - Temperatura Mínima (°C)
temp_max - Temperatura Máxima (°C)
chuva - Precipitação (mm)
fds - Final de Semana (1 = Sim; 0 = Não)
consumo - Consumo de Cerveja (litros)
'''

# Leitura dos dados
dados = pd.read_csv('Dados/Consumo_cerveja.csv',sep=';')

#Visualizar os dados
print(dados.head())

''' Variável Dependente x Variáveis Explicativas (pairplot) '''
# Gráficos de dispersão entre as variáveis do dataset
''' Plota o relacionamento entre pares de variáveis em um dataset. '''
ax = sns.pairplot(dados)
plt.show()

# Plotando o pairplot fixando somente uma variável no eixo y
ax = sns.pairplot(dados, y_vars = 'consumo', x_vars=['temp_min', 'temp_media', 'temp_max', 'chuva', 'fds'])
ax.fig.suptitle('Dispersão entre as Variáveis', fontsize = 16, y = 1.05)
plt.show()

ax = sns.pairplot(dados, y_vars = 'consumo', x_vars=['temp_min', 'temp_media', 'temp_max', 'chuva', 'fds'], kind='reg')
ax.fig.suptitle('Dispersão entre as Variáveis', fontsize = 16)
plt.show()