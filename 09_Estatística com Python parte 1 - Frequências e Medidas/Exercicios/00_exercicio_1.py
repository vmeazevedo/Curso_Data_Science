import pandas as pd 

dados = pd.DataFrame({'Profissão': [1, 2, 3, 1, 2, 2, 2, 3, 3, 2, 1, 3]})

'''
Onde a numeração representa as seguintes profissões:

1 para Estatístico
2 para Cientista de Dados
3 para Programador Python

Dada a seguinte distribuição de frequências: '''

# Visualizando os dados
print(dados.head())
# Visualizando os valores de frequencia 
print(dados['Profissão'].value_counts())
# Visualizando os valores de porcentagens
print(dados['Profissão'].value_counts(normalize = True)*100)

# Passandos os valores para variaiveis
frequencia = dados['Profissão'].value_counts()
porcentagem = dados['Profissão'].value_counts(normalize = True)*100

# Criando um novo dataframe com as variaveis
dist_freq_qualitativa = pd.DataFrame({'Frequência':frequencia, 'Porcentagem (%)': porcentagem})
print(dist_freq_qualitativa.head())

# Renomeando as linhas do index do DataFrame
dist_freq_qualitativa.rename(index = {1:'Estatístico', 2:'Cientista de Dados', 3:'Programador Python'}, inplace = True)
# Renomeando a coluna do index do DataFrame
dist_freq_qualitativa.rename_axis('Profissão', axis='columns', inplace=True)
print(dist_freq_qualitativa.head())
