import numpy as np

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

# Operações entre arrays e constantes
idade = 2020 - anos
print(idade)

# Operações entre arrays
km_media = km / idade
print(km_media)

# Operações com arrays de duas dimensões
dados = np.array([km, anos])
print(dados)

km_media = dados[0] / (2020 - dados[1])
print(km_media)