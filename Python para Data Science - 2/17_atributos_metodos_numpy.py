import numpy as np

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

dados = np.array([km, anos])
print(dados)

# ndarray.shape
''' Retorna uma tupla com as dimensoes do array.'''
print(dados.shape)

#ndarray.ndim
''' Retorna o numero de dimensoes do array.'''
print(dados.ndim)

#ndarray.size
''' Retorna o numero de elementos do array.'''
print(dados.size)

#ndarray.dtype
''' Retorna o tipo de dados do elementos do array.'''
print(dados.dtype)

#ndarray.T
''' Retorna o array transposto, isto é, converte linhas em colunas e vice versa.'''
print(dados.T)
print(dados.transpose())


# MÉTODOS
#ndarray.tolist()
''' Retorna o array como uma lista Python.'''
print(dados.tolist())

#ndarray.reshape(shape[, order])
''' Retorna um array que contém os mesmos dados com uma nova forma.'''
contador = np.arange(10)
print(contador)
print(contador.reshape((5,2)))
print(contador.reshape((5,2), order= 'C'))
print(contador.reshape((5,2), order= 'F'))

# Reshape a partir de uma lista
km = [44410., 5712., 37123., 0., 25757.]
anos = [2003, 1991, 1990, 2019, 2006]
info_carros = km + anos
print(info_carros)
print(np.array(info_carros).reshape((2,5)))


#ndarray.resize(new_shape[, refcheck])
''' Altera a forma e o tamanho do array'''
dados_new = dados.copy()
print(dados_new)
dados_new.resize((3,5), refcheck = False)
print(dados_new)


