'''
Considere o seguinte DataFrame para responder os próximos exercícios:
'''

import pandas as pd
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])

# Crie um DataFrame somente com os alunos aprovados.
selecao = alunos['Aprovado'] == True
n1 = alunos[selecao].shape[0]
print(n1)

# Crie um DataFrame somente com as alunas aprovadas.
selecao = (alunos['Aprovado'] == True) & (alunos['Sexo'] == 'F')
n2 = alunos[selecao].shape[0]
print(n2)

# Crie apenas uma visualização dos alunos com idade entre 10 e 20 anos ou com idade maior ou igual a 40 anos.
selecao = (alunos['Idade'] >= 10) & (alunos['Idade'] <= 20) | (alunos['Idade'] >= 40)
n3 = alunos[selecao].shape[0]
print(n3)