import numpy as np

km = np.loadtxt('data\\carros-km.txt')
anos = np.loadtxt('data\\carros-anos.txt', dtype = int)

#Obtendo km média por ano

km_media = km / (2019 - anos)

print(km_media)
print(type(km_media))

