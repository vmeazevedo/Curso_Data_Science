''' Relatório de Análise V
Tratamento de Dados Faltantes '''

import pandas as pd 

dados = pd.read_csv('dados\\aluguel_residencial.csv', sep = ';')
head = dados.head(10)
print(head)

# Verificando se a variavel é nula com o metodo isnull()
n1 = dados.isnull()
print(n1)

# Verificando se a variavel é nula com o metodo notnull()
n2 = dados.notnull()
print(n2)

# Identificando valor NaN em nosso dataset com o metodo info()
i = dados.info()
print(i)                    # Identificamos que temos valores NaN nas variaveis Valor, Condominio e IPTU

# Realizando uma seleção direta dos valores NaN da variavel Valor
n3 = dados[dados['Valor'].isnull()]
print(n3)                   # Apresentando os imoveis que tem o Valor como NaN

# Eliminando os registros NaN de nossa coluna Valor
A = dados.shape[0]          # Selecionamos o tamanho do nosso dataset antes da remoção
dados.dropna(subset = ['Valor'], inplace = True)    # Dropamos os NaN
B = dados.shape[0]          # Selecionamos o tamanho do nosso dataset depois da remoção
print("O numero de NaN removidos da coluna Valor foi de", A-B ,"registros.")

# Validando se ainda existe dados NaN em nossa coluna Valor
n4 = dados[dados['Valor'].isnull()]
print(n4)                   # Nos é retornado uma tabela vazia que confirma que os dados foram limpos