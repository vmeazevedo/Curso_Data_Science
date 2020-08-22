import pandas as pd 

data = [[1,2,3], [4,5,6],[7,8,9]]
print(data)

df = pd.DataFrame(data, list('321'), list('ZYX'))       # onde 321 é meu index e ZYX é minhas colunas
print(df)

# Organizando o meu index
df.sort_index(inplace=True)     # sort_index realiza um sorte do meu index organizando os dados em ordem
print(df)

# Organizando o meu index e as minhas colunas
df.sort_index(inplace=True, axis = 1)     # sort_index realiza um sorte organizando os dados em ordem
print(df)

# Organizando minhas colunas usando mais de uma variavel
df.sort_values(by = ['X', 'Y'], inplace=True)
print(df)

# Organizando meu index por uma variavel
df.sort_values(by = '3', axis = 1, inplace=True)
print(df)