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

# Verificando o tamanho do dataset
print(dados.shape)


''' Análises Preliminares '''
# Estastítiscas descritivas
print(dados.describe().round(2))


'''Matriz de correlação
O coeficiente de correlação é uma medida de associação linear entre duas variáveis e situa-se entre -1 e +1 sendo que 
-1 indica associação negativa perfeita e +1 indica associação positiva perfeita. '''
print(dados.corr().round(4))

'''Comportamento da Variável Dependente (Y)'''
# Análise gráficas
# Plotando a variável dependente (y)
fig, ax = plt.subplots(figsize=(15,5))

ax.set_title('Consumo de Cerveja', fontsize = 14)
ax.set_ylabel('Litros', fontsize = 12)
ax.set_xlabel('Dias', fontsize = 12)
ax = dados['consumo'].plot()
plt.show()

''' Box-Plot '''
# Box plot da variável dependente (y)
ax = sns.boxplot(data=dados['consumo'], orient='h')
ax.figure.set_size_inches(10,5)
ax.set_title('Consumo de Cerveja', fontsize = 14)
ax.set_ylabel('Litros', fontsize = 12)
plt.show()

''' Box-Plot com duas variáveis'''
# Investigando a variável dependente (y) segundo determinada característica
sns.set_palette("Accent")
sns.set_style("dark")
ax = sns.boxplot(y='consumo', x='fds', data = dados, orient='v', width=0.5)
ax.figure.set_size_inches(10,5)
ax.set_title('Consumo de Cerveja', fontsize = 14)
ax.set_ylabel('Litros', fontsize = 12)
ax.set_xlabel('Final de Semana', fontsize = 12)
plt.show()

''' Distribuição de Frequência '''
# Distribuição de frequênncias da variável dependente (y)
ax = sns.distplot(dados['consumo'])
ax.figure.set_size_inches(10,5)
ax.set_title('Distribuição de Frequência', fontsize = 14)
ax.set_ylabel('Consumo de Cerveja (Litros)', fontsize = 12)
plt.show()