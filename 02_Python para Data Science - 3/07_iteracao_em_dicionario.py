dados = {'Crossfox': 72832.16, 'DS5': 124549.07, 'Fusca': 150000, 'Jetta Variant': 88078.64, 'Passat': 106161.95}
print(dados)

# dict.keys()
'''Retorna uma lista contendo as chaves do dicionario.'''
print(dados.keys())

# dict.values()
'''Retorna uma lista com todos os valores do dicionarios.'''
print(dados.values())

# dict.items()
'''Retorna uma lista contendo uma tupla para cada par chave-valor do dicionario.'''
print(dados.items())

for key, value in dados.items():
    print(key, value)

for key, value in dados.items():
    if (value > 100000):
        print(key)