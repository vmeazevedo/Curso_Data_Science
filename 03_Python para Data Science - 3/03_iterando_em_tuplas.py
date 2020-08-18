# Iterando em tuplas
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')

for item in nomes_carros:
    print(item)

# Desacoplamento de tuplas
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
carro_1, carro_2, carro_3, carro_4 = nomes_carros

print(carro_1)
print(carro_2)
print(carro_3)
print(carro_4)

_, A, _, B = nomes_carros   # Selecionando somente os parametros da tupla que eu quero passar
print(A)
print(B)

_, C, *_ = nomes_carros     # Selecionando somente um parametro e ignorando os posteriores a ele
print(C)


# zip()
carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
valores = [88078.64, 106161.94, 72832.16, 124549.07]

print(list(zip(carros, valores)))           # Criamos uma tupla com os valores das listas acima

for item in zip(carros, valores):           # Iterando os dados da tupla
    print(item)

for carro, valor in zip(carros, valores):   # Iterando mais de um dado da tupla criada
    print(carro, valor)

for carro, valor in zip(carros, valores):   # Iterando usando um if para selecionar dados especificos
    if (valor >100000):
        print(carro)
    