import numpy as np

anos = np.loadtxt(fname = "data\\carros-anos.txt", dtype = int)
km = np.loadtxt(fname = "data\\carros-km.txt")
valor = np.loadtxt(fname = "data\\carros-valor.txt") 

dataset = np.column_stack((anos, km, valor))
print(dataset.shape)

# np.mean()
''' Retorna a media dos elementos do array ao longo do eixo especificado.'''
print(np.mean(dataset, axis = 0))

