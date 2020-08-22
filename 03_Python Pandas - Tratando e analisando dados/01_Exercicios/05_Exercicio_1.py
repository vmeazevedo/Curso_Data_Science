'''
Falando da criação de novas variáveis para um DataFrame, 
analise as opções abaixo e indique a que apresenta um erro durante a execução. 
Considere o DataFrame abaixo:
'''

import pandas as pd 

import pandas as pd
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas'])

a = alunos.head(10)
print(a)

# alunos['Notas-Média(Notas)'] = alunos['Notas'].apply(lambda x: x - alunos['Notas'].mean())
alunos['Notas-Média(Notas)'] = alunos.Notas - alunos.Notas.mean()

alunos['Faixa Etária'] = alunos['Idade'].apply(lambda x: 'Menor que 20 anos' if x < 20 else ('Entre 20 e 40 anos' if (x >= 20 and x <= 40) else 'Maior que 40 anos'))








print(alunos)

