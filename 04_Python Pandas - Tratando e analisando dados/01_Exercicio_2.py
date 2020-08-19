import pandas as pd 

dados = [[1, 2, 3], [4, 5, 6]]
index = 'X,Y'.split(',')
columns = list('CBA')[::-1]
df = pd.DataFrame(dados, index, columns)
print(df)

dados = {'A': {'X': 1, 'Y': 3}, 'B': {'X': 2, 'Y': 4}}
df = pd.DataFrame(dados)
print(df)