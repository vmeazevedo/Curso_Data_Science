import pandas as pd

dataset = pd.read_csv('data\\db.csv', sep = ';', index_col = 0)

# Verificando informações do ds
print(dataset.info())

# Verificando se um valor é nulo, ele retorna true
print(dataset.Quilometragem.isna())

# Verificando ao longo do dataset os valores de quilometragem nulos
print(dataset[dataset.Quilometragem.isna()])

# Alterando os valores de NaN para 0
dataset.fillna(0, inplace = True)
print(dataset)

# Validando se a alteração foi feita com uma querie
print(dataset.query("Zero_km == True"))


# Eliminando linhas que contenham NaN do meu dataset
dataset = pd.read_csv('data\\db.csv', sep = ';')
print(dataset)

dataset.dropna(subset = ['Quilometragem'], inplace = True)
print(dataset)
