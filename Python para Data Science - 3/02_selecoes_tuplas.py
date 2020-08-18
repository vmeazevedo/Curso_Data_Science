# Acessando indices em uma tupla
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
print(nomes_carros)

print(nomes_carros[0])
print(nomes_carros[-1])
print(nomes_carros[1:3])


# Acessando indices em uma tupla com uma tupla dentro
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5',('Fusca', 'Gol', 'C4'))
print(nomes_carros)
print(nomes_carros[-1])
print(nomes_carros[-1][1])