import pandas as pd 

dados = pd.read_csv('exemplo_df.csv',sep=';')
print(dados,"\n")

# Incluindo uma linha com dados no DataFrame
novo_dado = ['Espanha', 'Madrid', 99]
dados.loc[len(dados)] = novo_dado
print(dados,"\n")

# Incluindo uma coluna com dados no DataFrame
moeda_local = 'Euro','Peso','Peso','Real','Euro'
dados.insert(loc=3, column="Moeda", value=moeda_local)
print(dados,"\n")

# Deletando dados de um DataFrame
novo_df = dados.drop(labels=1)
print(novo_df,"\n")

# Renomeando o index
novo_df.index.names = ['Nº']
print(novo_df,"\n")

# Renomeando as colunas
novo_df.columns = ['Países', 'Capitais', 'População', 'Moeda']
print(novo_df)

# Exportando nosso nodo DataFrame
novo_df.to_csv('exemplo_df_1.csv', sep=';', index=False)