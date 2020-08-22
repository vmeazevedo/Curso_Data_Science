'''
Utilizando os recursos aprendidos nesta aula, julgue o conjunto de operações de limpeza do DataFrame abaixo:
'''
import pandas as pd 

imoveis = pd.DataFrame([['Apartamento', None, 970, 68], 
                        ['Apartamento', 2000, 878, 112], 
                        ['Casa', 5000, None, 500], 
                        ['Apartamento', None, 1010, 170], 
                        ['Apartamento', 1500, 850, None], 
                        ['Casa', None, None, None], 
                        ['Apartamento', 2000, 878, None], 
                        ['Apartamento', 1550, None, 228], 
                        ['Apartamento', 2500, 880, 195]], 
                        columns = ['Tipo', 'Valor', 'Condominio', 'IPTU'])
print(imoveis.head(10))

'''Tratando a coluna Valor'''
# Verificando valores null na coluna Valor
n1 = imoveis['Valor'].isnull()
print(n1)
print()

# Dropando os valores null da coluna Valor
A = imoveis.shape[0]
imoveis.dropna(subset = ['Valor'], inplace = True)
B = imoveis.shape[0]
print("- O numero de valores null removidos da coluna Valor foram:",A-B)
print()


'''Tratando a coluna Tipo'''
# Selecionando os apartamentos que tenham condominio null
print("- Removendo os imoveis do tipo Apartamento que nao apresentem o valor Condominio: ")
n2 = (imoveis['Tipo'] == 'Apartamento') & (imoveis['Condominio'].isnull())
print("\n- Valor removido: ")
print(imoveis[n2])
print("\n- Nosso dataset atual: ")
print(imoveis[~n2])
print()

# Substituindo os valores null em Condominio e IPTU por zero
print("- Substituindo os valors NaN por 0 em Condominio e IPTU:")
n3 = imoveis.fillna({'Condominio':0, 'IPTU':0})
print(n3)

# Organizando o index com o novo DataFrame
print("\n- Organizando o index com o novo DataFrame:")
n3.index = range(imoveis.shape[0])
print(n3)
