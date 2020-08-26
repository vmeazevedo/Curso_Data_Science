import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ranksums

''' Analise 5 - Hora do dia '''
gorjetas = pd.read_csv('data\\tips_tratados_4.csv',sep=',')
print(gorjetas.head())

print(gorjetas.hora_do_dia.unique())

sns.catplot(x='hora_do_dia',y='valor_da_conta',data=gorjetas)
plt.show()

# Espalha alguns pontos proximos de forma distribuida para uma melhor visualização
sns.catplot(x='hora_do_dia',y='valor_da_conta', kind='swarm',data=gorjetas)
plt.show()

# Demonstra a visualização em formato de violino, onde a maior concentração será apresentada na parte mais gorda
sns.violinplot(x='hora_do_dia',y='valor_da_conta',data=gorjetas)
plt.show()

# Demonstra a estatisticas do metodo describe de uma forma visual
sns.boxplot(x='hora_do_dia',y='valor_da_conta',data=gorjetas)
plt.show()

# Histograma = Um gráfico que tem, no eixo X, o valor da variável sendo exibida e no outro eixo, a frequência.
# Histograma do almoço
almoço = gorjetas.query("hora_do_dia == 'Almoço'").valor_da_conta
sns.distplot(almoço)
plt.show()

# Histograma do jantar
jantar = gorjetas.query("hora_do_dia == 'Jantar'").valor_da_conta
sns.distplot(jantar)
plt.show()

