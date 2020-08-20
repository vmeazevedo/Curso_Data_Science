import pandas as pd

numeros = [i for i in range(11)]
letras = [chr(i + 65) for i in range(11)]
nome_coluna = ['N']

df = pd.DataFrame(data = numeros, index = letras, columns = nome_coluna)
print(df)

selecao = df['N'].isin([i for i in range(11) if i % 2 == 0])
df = df[selecao]
print(df)
