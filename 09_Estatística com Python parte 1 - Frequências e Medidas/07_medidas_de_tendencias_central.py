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

''' Mediana
Para obtermos a mediana de um conjunto de dados devemos proceder da seguinte maneira:

1 - Ordenar o conjunto de dados;
2 - Identificar o numero de observações (registros) do conjunto de dados (n);
3 - Identificar o elemento mediano;

    Quando n for impar, a posição do elemento mediano sera obtida da seguinte forma:
                ElementoMd = n+1 / 2

    Quando n for par, a posição do elemento mediano será obtida da seguinte forma:
                ElementoMd = n/2 

4 - Obter a mediana:

    Quando n for impar:
                Md = X ElementoMd
    
    Quando n for par:
                Md = X ElementoMd + X ElementoMd+1 / 2
'''


# Exemplo
# Mediana com o metodo median
print(df['Fulano'].median())

# Mediana com o metodo quantile
print(df['Fulano'].quantile())
