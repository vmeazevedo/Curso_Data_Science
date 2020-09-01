import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Importando nossa base e lendo o dataset do projeot
dados = pd.read_csv('data\\dados.csv',sep=',')
print(dados.head())
print(dados.describe().round(2))

''' Box-plot

O box plot da uma ideia da posição, dispersão, assimetria, caudas e dados discrepantes.
A posição central é dada pela mediana e a dispersão por IIQ. As posições relativas de Q1,
Mediana, e Q3 dão uma noção da simetria da distribuição. Os comprimentos das caudas são
dados pelas linhas que vão do retângulo aos valores remotos e pelos valores atípicos. '''

# Analisando os boxplots
# ax = sns.boxplot(x= 'Altura', y = 'Sexo', data = dados, orient='h')
# ax.figure.set_size_inches(12,6)
# ax.set_title('Altura', fontsize = 18)
# ax.set_xlabel('Metros', fontsize = 14)
# plt.show()


sns.set_palette('Accent')                   
sns.set_style('darkgrid') 

ax = plt.subplot(2,1,1)
ax = sns.boxplot(x= 'Renda', y = 'Sexo', data = dados.query('Renda < 10000'), orient='h')
ax.figure.set_size_inches(12,6)
ax.set_title('Renda x Sexo', fontsize = 16)
ax.set_xlabel('R$', fontsize = 12)
# plt.show()
plt.subplot(2,1,2)
ax = sns.boxplot(x= 'Anos de Estudo', y = 'Sexo', data = dados, orient='h')
ax.figure.set_size_inches(12,6)
ax.set_title('Anos de Estudo x Sexo', fontsize = 16)
ax.set_xlabel('Anos', fontsize = 12)
plt.show()
