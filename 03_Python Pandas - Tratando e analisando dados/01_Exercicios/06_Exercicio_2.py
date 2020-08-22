'''
A criação de grupamentos com o método groupby() facilita bastante na 
sumarização das informações de um DataFrame. O método describe() aplicado
a um grupamento gera um conjunto de estatísticas descritivas bastante útil
no processo de análise de dados, conforme o exemplo abaixo:
'''

import pandas as pd 

precos = pd.DataFrame([['Feira', 'Cebola', 2.5], 
                        ['Mercado', 'Cebola', 1.99], 
                        ['Supermercado', 'Cebola', 1.69], 
                        ['Feira', 'Tomate', 4], 
                        ['Mercado', 'Tomate', 3.29], 
                        ['Supermercado', 'Tomate', 2.99], 
                        ['Feira', 'Batata', 4.2], 
                        ['Mercado', 'Batata', 3.99], 
                        ['Supermercado', 'Batata', 3.69]], 
                        columns = ['Local', 'Produto', 'Preço'])
print(precos)

produtos = precos.groupby('Produto')
d = produtos.describe().round(2)
print(d)

estatisticas = ['mean', 'std', 'min', 'max']
nomes = {'mean': 'Média', 'std': 'Desvio Padrão', 'min': 'Mínimo', 'max': 'Máximo'}
d = produtos['Preço'].aggregate(estatisticas).rename(columns = nomes).round(2)
print(d)