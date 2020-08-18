import pandas as pd

# Configurando o DS para apresentar 1000 linhas e 1000 colunas do arquivo csv
# pd.set_option('display.max_rows', 1000)
# pd.set_option('display.max_columns', 1000)

# Importando o DS
dataset = pd.read_csv('data\\db.csv', sep = ';')

# Apresentando as informações
print(dataset)

# Verificando os tipos dentro do meu DS
print(dataset.dtypes)

# Gerando a estatistica descritiva de parametros
print(dataset[['Quilometragem', 'Valor']].describe())

# Apresentando informações do DS
print(dataset.info())