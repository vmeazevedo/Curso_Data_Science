''' Relatório de Análise VI
Criando Novas Variáveis '''

import pandas as pd 

dados = pd.read_csv('dados\\aluguel_residencial_2.csv', sep=';')
h = dados.head(10)
print(h,"\n")

# Criando uma nova variavel de Valor Bruto, contendo o valor de valor + condiminio + iptu
dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']
h = dados.head(10)
print(h,"\n")

# Criando o valor do m² em uma nova coluna
dados['Valor m2'] = (dados['Valor'] / dados['Area']).round(2)       # Calculando o valor m² e arrendondando ele
h = dados.head(10)
print(h,"\n")

# Criando o valor bruto do m² em uma nova coluna
dados['Valor Bruto m2'] = (dados['Valor Bruto'] / dados['Area']).round(2)       # Calculando o valor m² e arrendondando ele
h = dados.head(10)
print(h,"\n")

# Identificando os tipos e reclassificando eles no tipo agregado
casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')    # .apply permite aplicarmos uma função para cada registro do nosso DF
d = dados.head(10)
print(d,"\n")

########################################################################################################
########################################################################################################
''' Excluindo Variáveis '''
dados_aux = pd.DataFrame(dados[['Tipo Agregado','Valor m2', 'Valor Bruto', 'Valor Bruto m2']])
print(dados_aux.head(10))

# Métodos de excluir valores no DataFrame
# del
del dados_aux['Valor Bruto']
print(dados_aux.head(10))

# .pop
dados_aux.pop('Valor Bruto m2')
print(dados_aux.head(10))

# .drop
dados_aux.drop(['Valor m2'], axis = 1, inplace=True)
print(dados_aux.head(10))
########################################################################################################
########################################################################################################

''' Excluindo Variáveis do nosso DataFrame '''
dados.drop(['Valor Bruto', 'Valor Bruto m2'], axis=1, inplace=True)
print(dados.head(10))

# Exportando o nosso novo dataframe
dados.to_csv('dados\\aluguel_residencial_3.csv', sep = ';', index = False)