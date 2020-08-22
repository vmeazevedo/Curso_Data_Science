import numpy as np

'''
Considerando o array idades:
'''
idades = np.array([10, 23, 45, 34, 25])

'''
Dentre as alternativas abaixo, quais são formas corretas de se obter a média aritmética das idades?
'''
print(np.sum(idades) / idades.size)
print(np.mean(idades))
print(idades.mean())