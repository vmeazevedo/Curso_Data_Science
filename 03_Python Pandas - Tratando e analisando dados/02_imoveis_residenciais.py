''' Relatorio de Analise III
Imoveis Residenciais'''

import pandas as pd 

dados = pd.read_csv('dados\\aluguel.csv', sep= ';')
d = dados.head(10)
print(d)

# Filtrando os dados para mostrar somente tipos residenciais
t = dados['Tipo']                                   # selecionando somente a coluna Tipo
print(t.drop_duplicates())                          # jogando fora as duplicadas
residencial = ['Quitinete','Casa','Apartamento','Casa de Condomínio','Casa de Vila']        # salvando os tipos residenciais em uma lista
print(residencial)

d = dados.head(10)                               # imprimindo o head novamente para compararmos
selecao = dados['Tipo'].isin(residencial)        # utilizando o isin para apresentar true quando o item corresponder com a nossa lista residencial
print(d)
print(selecao)

dados_residencial = dados[selecao]               # criando um novo dataframe e passando o nosso df selecao nele, ira ser apresentado somente tipos residenciais
print(dados_residencial.head(20))

# Reconstruindo o index no nosso novo dataframe
dados_residencial.index = range(dados_residencial.shape[0])     # nosso dataframe agora possui o index do seu respectivo tamanhando, tendo a ordem crescente correta.
print(dados_residencial)


''' Exportando a Base de Dados '''
dados_residencial.to_csv('dados\\aluguel_residencial.csv', sep=';' , index=False)       # exportando o arquivo csv, usamos o index false para manter a formatação que ja fizemos anteriormente

dados_residencial_2 = pd.read_csv('dados\\aluguel_residencial.csv', sep=';')            # importamos o arquivo em um novo dataframe somente para teste.
print(dados_residencial_2)