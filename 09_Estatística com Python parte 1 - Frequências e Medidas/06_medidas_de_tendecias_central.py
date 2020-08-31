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

''' Média aritmética
- É representado por micro, quando se refere a população e por X quando refere a amostra'''

# Calculando a media
print(df['Fulano'].mean())

# Pegando a media de renda separando por sexo
print(dados.groupby(['Sexo'])['Renda'].mean().round(2))