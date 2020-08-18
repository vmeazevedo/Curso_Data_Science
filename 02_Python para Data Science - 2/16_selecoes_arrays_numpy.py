import numpy as np

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

dados = np.array([km, anos])
print(dados)


'''
Dica:
ndarray[linha][coluna] ou ndarray[linha, coluna]
'''
# Imprimindo o 1990 de nosso array dados
print(dados[1][2])
print(dados[1 , 2])


# Fatiamento
contador = np.arange(10)
print(contador)

print(contador[1:4])        # imprimindo do indice 1 ao 3
print(contador[1:8:2])      # imprimindo do indice 1 ao 8 com passo 2
print(contador[::2])        # imprimindo somente os indices positivos usando o passo 2

# Fatiamento com nosso array
print(dados[:, 1:3])        # selecionamos todas as linhas com os : e depois indicamos o intervalo das colunas que vamos buscar


# Arrays com booleanos
print(dados[:, dados[1] > 2000])

