import pandas as pd 

# importando nossa base
data = pd.read_csv('01_Exercicios\\informacoes.csv', sep=';')

# organizando ela em um dataframe
df_A = pd.DataFrame(data)
print(df_A)
print()

# utilizando o sort_values para organizar por sexo e nome
df_B = df_A.sort_values(by = ['Sexo', 'Nome'])
print(df_B)

