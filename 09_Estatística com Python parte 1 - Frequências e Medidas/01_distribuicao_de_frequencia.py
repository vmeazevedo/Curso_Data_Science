import pandas as pd

# Importando nossa base e lendo o dataset do projeot
dados = pd.read_csv('data\\dados.csv',sep=',')
print(dados.head())

''' Distribuição de frequências para variáveis qualitativas '''

# Método 1
# Apresentando os dois valores presentes na coluna Sexo
print(dados['Sexo'].value_counts())
# Utilizando o normalize para apresentar o resultado em %
print(dados['Sexo'].value_counts(normalize = True)*100)

# Salvando as informações em variaveis
frequencia = dados['Sexo'].value_counts()
percentual = dados['Sexo'].value_counts(normalize = True)*100

# Criando um novo DataFrame com as variaiveis
dist_freq_qualitativas = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)':percentual.round(3)})
print(dist_freq_qualitativas.head())

# Alterando os valores de 0 e 1 na nossa coluna 
dist_freq_qualitativas.rename(index= {0: 'Masculino', 1:'Feminino'}, inplace=True)
# Renomeando a coluna sexo novamente
dist_freq_qualitativas.rename_axis('Sexo', axis='columns', inplace=True)
print(dist_freq_qualitativas.head())
