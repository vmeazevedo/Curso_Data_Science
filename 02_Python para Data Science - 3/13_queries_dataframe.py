import pandas as pd

dataset = pd.read_csv('data\\db.csv', sep = ';', index_col = 0)
print(dataset.head())

# Realizando uma querie por motores diesel
select = dataset.Motor == 'Motor Diesel'
print(select)

# Passando o select com uma consulta
print(dataset[select])

#Realizando uma querie com multiplos parametros, buscando motores diesel zero km.
select = dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)]
print(select)

# Realizando a mesma querie utilizando o método query
print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))
