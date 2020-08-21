import pandas as pd
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])

print(alunos)

# Crie um DataFrame somente com os alunos reprovados e mantenha neste DataFrame apenas as colunas Nome, Sexo e Idade, nesta ordem.
selecao = alunos['Aprovado'] == False
n1 = alunos[selecao]
print(n1.loc[:][['Nome','Sexo','Idade']])

# Crie uma visualização com os três alunos mais novos.
alunos.sort_values(by = ['Idade'], inplace=True)
print(alunos.iloc[:3])