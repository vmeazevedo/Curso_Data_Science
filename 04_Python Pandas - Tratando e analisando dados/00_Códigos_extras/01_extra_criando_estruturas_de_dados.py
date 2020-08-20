import pandas as pd 

'''SERIES'''
data = [1,2,3,4,5]
s = pd.Series(data)
print(s)

# Metodos para passar os dados de index em uma serie
'''Metodo 1'''
index = ['Linha' + str(i) for i in range(5)]
print(index)
s = pd.Series(data = data, index = index)
print(s)

'''Metodo 2'''
data = { 'Linha' + str(i): i+1 for i in range(5)}
print(data)
s = pd.Series(data)
print(s)



'''DATAFRAME'''
data = [[1,2,3],[4,5,6],[7,8,9]]
df1 = pd.DataFrame(data = data)
print(df1)

# Metodos para passar os dados de index em um dataframe
'''Metodo 1'''
index = ['Linha ' + str(i) for i in range(3)] 
columns = ['Coluna ' + str(i) for i in range(3)]
df1 = pd.DataFrame(data, index, columns)
print(df1)

'''Metodo 2'''
data = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}

df2 = pd.DataFrame(data)
print(df2)

'''Metodo 3'''
data = [(1,2,3),(4,5,6),(7,8,9)]
df3 = pd.DataFrame(data, index, columns)
print(df3)