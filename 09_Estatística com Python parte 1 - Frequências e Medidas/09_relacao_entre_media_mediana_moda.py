import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Importando nossa base e lendo o dataset do projeot
dados = pd.read_csv('data\\dados.csv',sep=',')
print(dados.head())

# DataFrame de exemplo
df = pd.DataFrame(data = {'Fulano' : [8, 10, 4, 8, 6, 10, 8],
                        'Beltrano': [10,2,0.5,1,3,9.5,10],
                        'Sicrano' : [7.5,8,7,8,8,8.5,7]},
                index = ['Matemática',
                        'Português',
                        'Inglês',
                        'Geografia',
                        'História',
                        'Física',
                        'Química'])
df.rename_axis('Matérias', axis = 'columns', inplace=True)
print(df)

''' Relação entre média, mediana e moda '''


# Avaliando a variável RENDA
ax = sns.distplot(dados.query('Renda < 20000').Renda)
ax.figure.set_size_inches(12,6)
plt.show()

Moda = dados.Renda.mode()[0]
print(Moda)
Mediana = dados.Renda.median()
print(Mediana)
Media = dados.Renda.mean()
print(Media)

# Avaliando a variável ALTURA
ax = sns.distplot(dados.Altura)
ax.figure.set_size_inches(12,6)
plt.show()

Moda = dados.Altura.mode()
print(Moda)
Mediana = dados.Altura.median()
print(Mediana)
Media = dados.Altura.mean()
print(Media)


# Avaliando a variável ANOS DE ESTUDOS
ax = sns.distplot(dados['Anos de Estudo'], bins= 17)
ax.figure.set_size_inches(12,6)
plt.show()

Moda = dados['Anos de Estudo'].mode()[0]
print(Moda)
Mediana = dados['Anos de Estudo'].median()
print(Mediana)
Media = Mediana = dados['Anos de Estudo'].mean()
print(Media)