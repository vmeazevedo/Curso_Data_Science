import pandas as pd 

''' Estrutura de Dados '''
# Série
s = pd.Series([3,2,1], index=['a','b','c'])
print(s,"\n")

# Criando um DataFrame
data = {
    'País': ['Portugal', 'Peru', 'Chile'],
    'Capital': ['Lisboa', 'Lima', 'Santiago']
}

df = pd.DataFrame(data, columns=['País', 'Capital'])
print(df,"\n")

# Incluindo um dados no DataFrame
novo_dado = ['Brasil', 'Brasilia']
df.loc[len(df)] = novo_dado
print(df,"\n")

# Incluindo uma coluna com dados no DataFrame
habitantes = 9,8,6,4
df.insert(loc=2, column="População", value=habitantes)
print(df,"\n")

# Deletando dados de um DataFrame
novo_df = df.drop(labels=1)
print(novo_df,"\n")

# Renomeando o index
novo_df.index.names = ['Nº']
print(novo_df,"\n")

# Renomeando as colunas
novo_df.columns = ['Países', 'Capitais', 'Populações']
print(novo_df)
