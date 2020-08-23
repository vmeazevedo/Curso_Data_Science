import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

tmdb = pd.read_csv('ml-latest-small\\tmdb_5000_movies.csv')
print(tmdb.head())

# Variaveis categoricas nominal
print(tmdb.original_language.unique()) 

''' Analisando as demais linguas que não sejam ingles '''
total_por_lingua_de_outros_filmes = tmdb.query("original_language != 'en'").original_language.value_counts()
filmes_sem_lingua_original_em_ingles = tmdb.query("original_language != 'en'")
sns.catplot(x='original_language', kind='count', data = filmes_sem_lingua_original_em_ingles)
plt.show()

