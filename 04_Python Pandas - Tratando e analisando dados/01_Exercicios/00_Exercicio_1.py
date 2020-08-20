'''
Considere o seguinte código Python no Jupyter:
'''
import pandas as pd

data = [['Fulano', 12, 7.0, True],
        ['Sicrano', 15, 3.5, False], 
        ['Beltrano', 18, 9.3, True]]
dados = pd.DataFrame(data, columns = ['Aluno', 'Idade', 'Nota', 'Aprovado'])

print(dados)

'''
Para obtermos uma tabela contendo os nomes das variáveis e seus respectivos tipos de dados, conforme o exemplo abaixo, que linhas de código devemos executar no Jupyter?
'''
print()
tipo_dados = pd.DataFrame(dados.dtypes, columns= ['Tipos de Dados'])        # Apresentando as informações dos tipos de dados e nomeando a coluna
tipo_dados.columns.name = 'Variáveis'                                       # Renomeando a coluna 0 com o nome de Variaiveis
print(tipo_dados)