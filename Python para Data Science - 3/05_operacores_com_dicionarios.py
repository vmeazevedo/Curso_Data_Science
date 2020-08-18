dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

# dict[key]
''' Retorna o valor correspondente a chave key no dicionario'''
print(dados['Passat'])

# key in dict
''' Retorna True se a chave key for encontrada no dicionario'''
if 'Passat' in dados:
    print("True")
else:
    print("False")

if 'Fusca' not in dados:
    print("True")
else:
    print("False")

# len(dict)
''' Retorna o numero de itens do dicionario'''
print(len(dados))

# dict[key] = value
'''Inclui um item ao dicionario'''
dados['DS5'] = 124549.07
print(dados)

# del dict[key]
''' Remove o item de chave key do dicionario'''
del dados['Passat']
print(dados)

