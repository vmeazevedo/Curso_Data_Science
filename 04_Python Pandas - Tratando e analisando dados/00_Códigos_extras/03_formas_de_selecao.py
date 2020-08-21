import pandas as pd

data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (8, 10, 11, 12),
        (13, 14, 15, 16)]
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())       # Passmos o split como index e como columns
print(df)

# Apresentando as informações de somente a coluna C1
# Esse modo apresenta em uma Series
df2 = df['c1']
print(df2)

# Apresentando as informaçãoes de mais de uma coluna na ordem que quisermos
# Esse modo apresenta um DataFrame
df3 = df[['c3','c1']]
print(df3)

# Selecionando as linhas do index
# df4 = df[:]                     # selecionando todas as linhas
df4 = df[1:]                    # selecionando a partir do index 1 em diante
df4 = df[1:3]                   # selecionando um intervalo entre o index 1 e 2           
print(df4)

# Selecionando as linhas do index de uma determinada coluna
df5 = df[1:][['c3','c1']]
print(df5)


'''.loc()'''
# Realizando uma seleção a partir do rótulo das linhas utilizando o metodo .loc()
df6 = df.loc['l3']
print(df6)

# Selecionando mais de um rótulo de linha utilizando o metodo .loc()
df7 = df.loc[['l3','l2']]
print(df7)

# Identificando o valor do dados cruzando a linha e coluna com o metodo .loc()
df8 = df.loc['l1','c2']
print(df8)

# Selecionando dados cruzandos entre linha e coluna com o metodo .loc()
df88 = df.loc[['l3','l1'], ['c4','c1']]
print(df88)


'''.iloc()'''
# Identificando o valor do dados cruzando os indices da linha e coluna com o metodo .iloc()
df9 = df.iloc[0,1]
print(df9)

# Selecionando dados cruzandos entre linha e coluna com o metodo .loc()
df99 = df.iloc[[2,0], [3,0]]
print(df99)