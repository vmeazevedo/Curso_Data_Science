import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Importando nossa base e lendo o dataset do projeot
dados = pd.read_csv('data\\dados.csv',sep=',')

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

''' Variância

A variância é construida a partir das diferenças entre cada observação e a média dos dados, ou seja, o desvio em torno 
da média. No cálculo da variância, os desvios em torno da média são elevados ao quadrado.'''

# Variância populacional

# Variância amostral
# Pegamos as notas da coluna Fulano e colamos em um dataframe
notas_fulano = df[['Fulano']]
print(notas_fulano)

# Apresentando a variancia com o metodo var
variancia = notas_fulano['Fulano'].var()
print(variancia)

