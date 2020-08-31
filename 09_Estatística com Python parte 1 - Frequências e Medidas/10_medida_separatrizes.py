import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Importando nossa base e lendo o dataset do projeot
dados = pd.read_csv('data\\dados.csv',sep=',')
print(dados.head())

''' Quartis, decis e percentis '''

''' Há uma serie de medidas de posição semelhantes na sua concepção a mediana, embora não sejam medidas de tendencia central.
Como se sabe, a mediana divide a distribuição em duas partes iguais quanto ao numero de elementos de cada parte.
Já os quartis, permitem dividir a distribuição em quatro partes iguais quanto ao numero de elementos de cada uma;
os decis em dez partes e os percentis em cem partes iguais. '''

# Apresentando os valores dos quartis
print(dados.Renda.quantile([0.25, 0.50, 0.75]))

# Apresentando os valores dos decis
print(dados.Renda.quantile([i / 10 for i in range(1,10)]))

# Apresentando os valores dos percentis
print(dados.Renda.quantile([i / 100 for i in range(1,100)]))


ax = sns.distplot(dados.Idade,
                    hist_kws = {'cumulative':True},
                    kde_kws ={'cumulative':True},
                    bins = 10) 
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição de Frequência Acumulada', fontsize = 18)
ax.set_xlabel('Acumulado', fontsize = 14)
ax.set_xlabel('Anos', fontsize = 14)
plt.show()