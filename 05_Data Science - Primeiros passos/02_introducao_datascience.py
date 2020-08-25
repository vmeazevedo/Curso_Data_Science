import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

tmdb = pd.read_csv('ml-latest-small\\tmdb_5000_movies.csv')
print(tmdb.head())

# Variaveis categoricas nominal
print(tmdb.original_language.unique()) 

# primeiro grau
# segundo grau
# terceiro grau
# 1 < 2 < 3 categorica ordinal

# Budget => orçamento => quantitativo continuo
# Quantidade de votos => quantitativo, sem voto quebrado[float]

# Analisando quantas vezes uma lingua aparece em nossa base
contagem_de_lingua = tmdb.original_language.value_counts().to_frame().reset_index()     # Contamos quantas vezes aparece/ transformamos em um DF / resetamos o index
contagem_de_lingua.columns =  ['original_language', 'total']                            # Renomeamos as colunas do DF
print("\n",contagem_de_lingua.head())

# Imprimindo os dados analisados de lingua x frequencia de aparição
sns.barplot(x="original_language", y="total", data = contagem_de_lingua)
plt.show()


''' Metodo mais simples de fazer o trabalho anterior utilizando o catplot com o seaborn '''
# Imprimindo os dados analisados de lingua x frequencia de aparição
sns.catplot(x = "original_language", kind="count", data= tmdb)
plt.show()


''' A partir dos dados analisamos vamos agora apresentar que temos muito mais filmes em ingles
que em outras linguas '''
# Tratando os dados para separarmos o total de ingles e o resto das outras linguas
total_por_lingua = tmdb['original_language'].value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc['en']
total_do_resto = total_geral - total_de_ingles
print(total_de_ingles, total_do_resto)

# Criamos um dicionario com os valores captados
dados = {
    'lingua': ['Ingles', 'Outras linguas'],
    'total': [total_de_ingles, total_do_resto]
}

# Transformamos nosso dicionario em um DataFrame
df = pd.DataFrame(dados)

# Imprimimos o gráfico com as informações desejadas
sns.barplot(x = 'lingua', y='total', data=df)
plt.show()


''' Analisando as demais linguas que não sejam ingles '''
total_por_lingua_de_outros_filmes = tmdb.query("original_language != 'en'").original_language.value_counts()
filmes_sem_lingua_original_em_ingles = tmdb.query("original_language != 'en'")
sns.catplot(x='original_language', kind='count', data = filmes_sem_lingua_original_em_ingles)
plt.show()