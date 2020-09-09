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

''' Variável Dependente x Variáveis Explicativas (lmplot) '''
''' Plota a reta de regressão entre duas variáveis juntamente com a dispersão entre elas. '''
ax = sns.lmplot(x='temp_max', y='consumo', data=dados)
ax.fig.suptitle('Reta de Regressão - Consumo x Temperatura', fontsize = 16, y=1.05)
ax.set_xlabels('Temperatura Máxima (°C)', fontsize = 14)
ax.set_ylabels('Consumo de Cerveja (litros)', fontsize = 14)
plt.show()

# Plotando um lmplot utilizando uma terceira variável na análise (tipo I)
ax = sns.lmplot(x='temp_max', y='consumo', data=dados, hue='fds', markers=['o', '*'], legend=False)
ax.fig.suptitle('Reta de Regressão - Consumo x Temperatura', fontsize = 16, y=1.05)
ax.set_xlabels('Temperatura Máxima (°C)', fontsize = 14)
ax.set_ylabels('Consumo de Cerveja (litros)', fontsize = 14)
ax.add_legend(title='Fim de Semana')
plt.show()

# Plotando um lmplot utilizando uma terceira variável na análise (tipo II)
ax = sns.lmplot(x='temp_max', y='consumo', data=dados, hue='fds', col='fds')
ax.fig.suptitle('Reta de Regressão - Consumo x Temperatura', fontsize = 16, y=1.05)
ax.set_xlabels('Temperatura Máxima (°C)', fontsize = 14)
ax.set_ylabels('Consumo de Cerveja (litros)', fontsize = 14)
ax.add_legend(title='Fim de Semana')
plt.show()
