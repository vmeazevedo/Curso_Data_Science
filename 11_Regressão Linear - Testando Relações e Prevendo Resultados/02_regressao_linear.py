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

''' Variável Dependente x Variáveis Explicativas (joinplot) '''
''' Plota o relacionamento entre duas variáveis e suas respectivas distribuições de frequência.'''
sns.set_palette("Accent")
sns.set_style("dark")

ax = sns.jointplot(x='temp_max', y='consumo', data=dados)
ax.fig.suptitle('Dispersão - Consumo x Temperatura', fontsize = 18, y=1.05)
ax.set_axis_labels('Temperatura Máxima', 'Consumo de Cerveja', fontsize=14)
plt.show()

# Plotando um joinplot com a reta de regressão estimdada
ax = sns.jointplot(x='temp_max', y='consumo', data=dados, kind='reg')
ax.fig.suptitle('Dispersão - Consumo x Temperatura', fontsize = 18, y=1.05)
ax.set_axis_labels('Temperatura Máxima', 'Consumo de Cerveja', fontsize=14)
plt.show()
