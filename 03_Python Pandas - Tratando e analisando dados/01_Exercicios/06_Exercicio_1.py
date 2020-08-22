'''
Considere o seguinte DataFrame para responder o exercício abaixo:

Como devemos proceder para obter um DataFrame com as notas médias dos alunos, com duas casas decimais, segundo seu sexo?
'''

import pandas as pd 
 
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])

print(alunos)

sexo = alunos.groupby('Sexo')                       # Criamos um grupo com os dados da coluna Sexo
sexo = pd.DataFrame(sexo['Notas'].mean().round(2))  # Criamos um dataframe com os valores das medias das notas arredondadas em duas casas
sexo.columns = ['Notas Médias']                     # Informamos que a coluna ira chamas Notas Medias
print(sexo)

