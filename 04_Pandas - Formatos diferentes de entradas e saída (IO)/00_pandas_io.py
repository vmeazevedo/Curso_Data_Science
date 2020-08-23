import pandas as pd 

# Importamos nossa base de dados do IBGE
nomes_m = pd.read_json("https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking?qtd=200&sexo=m")
nomes_f = pd.read_json("https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking?qtd=200&sexo=f")

# Imprimimos o head
print(nomes_m.head())
print(nomes_f.head())
print("A quantidade de nomes: " + str(len(nomes_f) + len(nomes_m)))

# Passando os dados em uma variavel como uma lista
frames = [nomes_f, nomes_m]

# Utilizando o metodo .concat para concatenar as duas listas, e utilizando o metodo .to_frame para transformar isso em um DF
# Passamos que queremos trabalhar somente com a coluna ['nome]
nomes = pd.concat(frames)['nome'].to_frame() 

# Apresentando alguns nomes aleatórios
print(nomes.sample(5))

