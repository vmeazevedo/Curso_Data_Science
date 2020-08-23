import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Importando nossa base
notas = pd.read_csv('ml-latest-small\\ratings.csv')
notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']     # Renomemando as colunas
filmes = pd.read_csv('ml-latest-small\\movies.csv')
filmes.columns = 'filmeId','titulo','genero'                    # Renomemando as colunas
# print(notas.head())
print(filmes.head(2))

# Realizando uma query e pegando todas as notas dos filmeid 1 e 2
notas_toy_story = notas.query('filmeId == 1')
notas_jumanji = notas.query('filmeId == 2')

print(len(notas_toy_story), len(notas_jumanji))

# Calculando a media do filmeid 1 e 2
print("\nNota média do Toy Story ", notas_toy_story.nota.mean().round(3))
print("Nota média do Toy Jumanji ", notas_jumanji.nota.mean().round(3))

# Apresentando o boxplot com os valores do filmeid
t = notas_toy_story.nota.describe()
j = notas_jumanji.nota.describe()
print("\nEstatisticas do filme Toy Story:\n",t)
print("\nEstatisticas do filme Jumanji:\n",j)
sns.boxplot(x = "filmeId", y = "nota", data = notas.query("filmeId in [1,2]"))
plt.title("Boxplot dos filmes Toy Story e Jumanji")
plt.show() 