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
nomes['id_aluno'] = np.random.permutation(total_alunos) + 1     # Destribuindo os valores aleatóriamente dentro da base  
print(nomes.head())

# Criando a coluna dos dominios dos e-mails
dominios = ['@dominiodoemail.com.br', '@servicodoemail.com']    # Criamos uma lista com os valores de dominios que vamos usar
nomes['dominio'] = np.random.choice(dominios, total_alunos)     # Utilizamos o metodo .choice para escolher aleatoriamente entre eles para cada aluno
print(nomes.head())
 
# Criando a coluna de e-mails
nomes['email'] = nomes.nome.str.cat(nomes.dominio).str.lower()
print(nomes.head())


''' Criando a tabela cursos '''
import html5lib

# Buscando uma tabela especifica dentro de um site
url = 'http://tabela-cursos.herokuapp.com/index.html'
cursos = pd.read_html(url)                  # Passamos o link do site para selecionarmos a tabela que vamos usar
print(cursos)

# Transformando a lista cursos em um Dataframe
cursos = cursos[0]
print(cursos.head(5))

# Alterando o nome da coluna
cursos.columns = ['nome_do_curso']          # quando temos uma coluna só podemos usar esse modo
# cursos = cursos.rename(columns = {'Nome do curso' : 'nome_do_curso'})     # modo mais complicado rs
print(cursos.head())

# Criando uma coluna para ser o index
cursos['id'] = cursos.index + 1
print(cursos.head())

# Usando a coluna id como index do DataFrame
cursos = cursos.set_index('id')
print(cursos.head())


''' Matriculando os alunos nos cursos '''
import seaborn as sns
import matplotlib.pyplot as plt

print("\n",nomes.head())

# Criando o numero aleatorio de matriculas em cursos diferentes por alunos
nomes['matriculas'] = np.ceil(np.random.exponential(size = total_alunos) * 1.5).astype(int)
print("\n",nomes.head())

# Verificando as estatisicas de nosso DataFrame
print(nomes.describe())

# Verificando a quantidade apresentada no describe com o histograma
# sns.distplot(nomes.matriculas)
# plt.show()

# Verificando as quantidades exatas com o value_counts()
print(nomes.matriculas.value_counts())


''' Selecionando cursos '''
print("\n",nomes.head())

todas_matriculas = []               
x = np.random.rand(20)
prob = x / sum(x)

for index, row in nomes.iterrows():
    id = row.id_aluno
    matriculas = row.matriculas
    for i in range(matriculas):
        mat = [id, np.random.choice(cursos.index, p = prob)]
        todas_matriculas.append(mat)

matriculas = pd.DataFrame(todas_matriculas, columns= ['id_aluno', 'id_curso'])
print(matriculas.head())

matriculas_por_curso = matriculas.groupby('id_curso').count().join(cursos['nome_do_curso']).rename(columns={'id_aluno':'quantidade_de_alunos'})
print(matriculas.head())

print(nomes.sample(3))
print(cursos.head(3))
print(matriculas.head(3))
print(matriculas_por_curso.head(3)) 


''' Saida em diferentes formatos '''

# Exportando em csv
matriculas_por_curso.to_csv('matriculas_por_cursos.csv', index=False)
pd.read_csv('matriculas_por_cursos.csv')

# Exportando o json em uma variavel
matriculas_json = matriculas_por_curso.to_json()

# Exportando o html em uma variavel
matriculas_html = matriculas_por_curso.to_html()
