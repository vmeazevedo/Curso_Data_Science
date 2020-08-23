import pandas as pd 

dados = pd.read_csv('exemplo_df.csv',sep=';')
print(dados,"\n")

# Seleciona um único valor por linha & coluna
d = dados.iloc[0][0]
print(d,'\n')

# Seleciona um único valor por rótulo de linha & coluna
d = dados.iloc[0]['Pais']
print(d,'\n')
