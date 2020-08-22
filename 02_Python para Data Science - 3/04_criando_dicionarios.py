carros = ['Jetta Variant', 'Passat', 'Crossfox']
valores = [88078.64, 106161.94, 72832.16]

# Criando um dicionário
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
print(dados)
print(type(dados))

# Criando dicionario com zip()
dados = dict(zip(carros, valores))
print(dados)

