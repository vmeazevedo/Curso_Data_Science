'''Analisando algumas notas especificas por filme '''

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Importando nossa base
notas = pd.read_csv('ml-latest-small\\ratings.csv')
notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']     # Renomemando as colunas
filmes = pd.read_csv('ml-latest-small\\movies.csv')
filmes.columns = 'filmeId','titulo','genero'                    # Renomemando as colunas
print(notas.head())
print(filmes.head())

''' Realizando uma busca de um filme especifico com o query '''
# Trabalhando com query, pesquisando informações dos filmes em nossa base
id1 = notas.query("filmeId==1").nota.mean().round(3)        # Pegando a nota media do filmeId 1
print(f"\nA nota media do filmeId 1 é de: {id1}")

id2 = notas.query("filmeId==2").nota.mean().round(3)        # Pegando a nota media do filmeId 1
print(f"\nA nota media do filmeId 2 é de: {id2}")

''' Colocando todas as notas em um grupo para facilitar a nossa analise '''
# Agrupando as notas pela coluna filme
medias_por_filme = notas.groupby("filmeId").mean()["nota"].round(3)
print("\n",medias_por_filme.head())

''' Plotando algumas informações analisadas '''
# Apresentando o histograma das medias x filme
# medias_por_filme.plot(kind='hist')              # Uma das formas de plotar o histograma com matplotlib
# plt.show()

# Apresentando o describe e o boxplot das medias x filme
print("\n",medias_por_filme.describe())
sns.boxplot(medias_por_filme)
plt.title("Boxplot das medias dos filmes")
plt.show()

# Apresentando o histograma com o seaborn e matplotlib
sns.distplot(medias_por_filme)
plt.title("Histograma das medias dos filmes")
plt.show()
plt.hist(medias_por_filme)
plt.title("Histograma das medias dos filmes")
plt.show()


