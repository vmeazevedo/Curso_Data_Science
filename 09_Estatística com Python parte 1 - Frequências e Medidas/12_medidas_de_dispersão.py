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

''' Medidas de dispersão

Embora as medidas de posição forneçam uma sumarização bastante importante dos dados,
elas podems não ser suficientes para caracterizar conjuntos distintos, especialmente
quando as observações de determinada distribuição apresentarem dados muitos dispersos.
'''

# Desvio médio absoluto
# Pegamos as notas da coluna Fulano e colamos em um dataframe
notas_fulano = df[['Fulano']]
print(notas_fulano)

# Utilizamos o metodo mad para calcular o desvio absoluto
desvio_medio_absoluto = notas_fulano['Fulano'].mad()
print(desvio_medio_absoluto)