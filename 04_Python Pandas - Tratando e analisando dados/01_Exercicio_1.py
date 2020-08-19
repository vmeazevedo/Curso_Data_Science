import pandas as pd

# Criando um dataset
dados = pd.DataFrame([1,1,2,3,3,3,4,4], columns = ['X'])
print(dados)

# Removendo as duplicadas de nosso dataset
print("Dados sem as duplicadas")
dados.drop_duplicates(inplace=True)
print(dados)