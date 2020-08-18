import pandas as pd

dataset = pd.read_csv('data\\db.csv', sep = ';', index_col = 0)
# print(dataset.head())

for index, row in dataset.iterrows():
    if(2019 - row['Ano'] != 0):
        
        s = dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2019 - row['Ano'])

    else:
        s = dataset.loc[index, 'Km_media'] = 0
