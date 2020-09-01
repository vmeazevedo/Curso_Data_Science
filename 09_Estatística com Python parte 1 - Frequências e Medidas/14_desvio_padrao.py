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

''' Desvio padrão

Uma das restrições da variãncia é o fato de fornecer medidas em quadrados das unidades originais
a variancia de medidas de comprimento, por exemplo, é em unidades de area. Logo, o fato de as unidades
serem diferentes dificulta a comparação da dispersão com as variáveis que a definem. Um modo de eleminar
essa dificuldade é considerar sua raiz quadrada.'''

# Desvio padrão amostral
# Pegamos as notas da coluna Fulano e colamos em um dataframe
notas_fulano = df[['Fulano']]
print(notas_fulano)

desvio_padrão = notas_fulano['Fulano'].std()
print(desvio_padrão)