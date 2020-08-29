import pandas as pd

# Importando nossa base e lendo o dataset do projeot
dados = pd.read_csv('data\\dados.csv',sep=',')
print(dados.head())

''' Distribuição de frequências para variáveis qualitativas '''

# Método 2
sexo = {0:'Masculino',
        1:'Feminino'}

cor = {0: 'Indígena',
        2: 'Branca',
        4: 'Preta',
        6: 'Amarela',
        8: 'Parda',
        9: 'Sem declaração'}

# Plotando a frequencia com o metodo crosstab
frequencia = pd.crosstab(dados.Sexo, dados.Cor)
frequencia.rename(index = sexo, inplace=True)
frequencia.rename(columns = cor, inplace=True)
print(frequencia)

# Plotando a porcentagem com o metodo crosstab
percentual = pd.crosstab(dados.Sexo, dados.Cor, normalize=True) *100
percentual.rename(index = sexo, inplace=True)
percentual.rename(columns = cor, inplace=True)
print(percentual.round(2))