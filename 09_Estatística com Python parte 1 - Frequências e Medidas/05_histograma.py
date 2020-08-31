import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Importando nossa base e lendo o dataset do projeot
dados = pd.read_csv('data\\dados.csv',sep=',')
print(dados.head())

''' O histograma é a representação gráfica de uma distribuição de frequencias.
É um grafico formado por um conjunto de retangulos colocados lado a lado, onde
a area de cada retangulo é proporcional a frequencia da classe que ele representa.'''

# Criando um histograma com os dados de altura com o seaborn
ax = sns.distplot(dados.Altura)
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição de Frequência - Altura', fontsize = 18)
ax.set_xlabel('Metros', fontsize = 14)
plt.show()

# Criando um histograma com os dados de altura com o pandas
dados.Altura.hist(bins=50, figsize=(12,6))
plt.show()