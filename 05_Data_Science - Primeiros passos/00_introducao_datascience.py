import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Importando nossa base
notas = pd.read_csv('ml-latest-small\\ratings.csv')
print(notas.head())

# Verificando o tamanho dela
n1 = notas.shape
print(f"\n A quantidade de dados em nossa base é de {n1}\n")

# Renomeando as colunas
notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']
print(notas.head())

# Verificando as notas que foram dadas em nossos dados
print("\nAs nota encontradas em nossa base foram: ")
print(notas['nota'].unique())

# Verificando quantas vezes as notas foram dadas
print("\nA quantidade de apontamentos por notas foi: ")
print(notas['nota'].value_counts())

# Verificando a média e a mediana de todas as notas
print("\nMedia",notas['nota'].mean().round(2))
print("Mediana",notas['nota'].median().round(2))

# Apresentando um histograma das notas que foram dadas x quantidades
notas.nota.plot(kind='hist')
plt.show()

# Analisando os valores das notas com o metodo .describe()
print(notas.nota.describe())

# Apresentando a frequencia das informações com o boxplot   
sns.boxplot(notas.nota)
plt.show()