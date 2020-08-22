# IF ELSE

# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2009, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]


zero_km_Y, zero_km_N = [], []

for lista in dados:
    if (lista[2] == True):
        zero_km_Y.append(lista)
    else:
        zero_km_N.append(lista)

print(zero_km_Y)
print(zero_km_N)


# ELIF
dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2009, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]

A, B, C = [], [], []

for lista in dados:
    if (lista[1] <= 2000):
        A.append(lista)
    elif (lista[1] > 2000 and lista[1] <= 2010):
        B.append(lista)
    else:
        C.append(lista)
print(A)
print(B)
print(C)