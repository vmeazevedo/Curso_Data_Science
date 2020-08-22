''' Relatório de Análise V
Tratamento de Dados Faltantes '''

import pandas as pd 

dados = pd.read_csv('dados\\aluguel_residencial_2.csv', sep = ';')
head = dados.head(10)
print(head)

# Verificando se a variavel é nula com o metodo isnull()
n1 = dados.isnull()
print(n1)

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
print()


''' Tratamento de Dados Faltantes '''
# Selecionando a coluna Condominio com valores nulos
n5 = dados[dados['Condominio'].isnull()].shape[0]
print("A quantidade de condominios com valores nulos são:",n5)                   # Identificando a quantidade de condominio nulos

# Selecionando os Apartamentos que tenham Condominio nulo
selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())

# Eliminando os registros de Apartamentos que contenham Condominio NaN de nossa selecao
A = dados.shape[0]          # Selecionamos o tamanho do nosso dataset antes da remoção
dados = dados[~selecao]     # Utilizamos o ~ para selecionar somente aqueles que não são NaN
B = dados.shape[0]          # Selecionamos o tamanho do nosso dataset depois da remoção
print("O numero de apartamentos que tem condomínio nulos é", A-B ,"registros.")

# Verificando a quantidades restante de Condominio com valores nulos em nosso dataset
n5 = dados[dados['Condominio'].isnull()].shape[0]
print("Ainda temos", n5,"condominios nulos.")                   # Identificando a quantidade de condominio nulos

# Alterando os valores de NaN de Condominio e IPTU para 0
dados = dados.fillna({'Condominio': 0, 'IPTU': 0})
n7 = dados[dados['Condominio'].isnull()].shape[0]
n8 = dados[dados['IPTU'].isnull()].shape[0]
print(f"O numero de condominio com valores nulos é {n7}, e o numero de IPTU com valores nulos é {n8}")

# Identificando se ainda temos valor NaN em nosso dataset com o metodo info()
i = dados.info()
print(i)

# Exportando o nosso novo dataframe
dados.to_csv('dados\\aluguel_residencial_2.csv', sep = ';', index = False)