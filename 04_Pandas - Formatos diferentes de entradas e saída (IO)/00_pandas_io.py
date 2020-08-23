''' Criando os nomes '''
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

''' Incluindo ID dos alunos '''
import numpy as np

# Gerando numeros aleatorio com numpy
np.random.seed(123)

# Criando os ids dos alunos
total_alunos = len(nomes)                                       # Pegamos o numero de linhas da base
nomes['id aluno'] = np.random.permutation(total_alunos) + 1     # Destribuindo os valores aleatóriamente dentro da base  
print(nomes.head())

# Criando a coluna dos dominios dos e-mails
dominios = ['@dominiodoemail.com.br', '@servicodoemail.com']    # Criamos uma lista com os valores de dominios que vamos usar
nomes['dominio'] = np.random.choice(dominios, total_alunos)     # Utilizamos o metodo .choice para escolher aleatoriamente entre eles para cada aluno
print(nomes.head())
 
# Criando a coluna de e-mails
nomes['email'] = nomes.nome.str.cat(nomes.dominio).str.lower()
print(nomes.head())

print(nomes.count())