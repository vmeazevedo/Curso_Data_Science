from scipy.stats import norm

'''
A aplicação de uma prova de estatística em um concurso apresentou um conjunto de notas normalmente distribuídas. 
Verificou-se que o conjunto de notas tinha média 70 e desvio padrão de 5 pontos.

Qual a probabilidade de um aluno, selecionado ao acaso, ter nota menor que 85?
'''

# Obter a variavel padronizada Z
media = 70
desvio_padrao = 5
Z = (85 - media) / desvio_padrao
print(f'valor de Z = {Z}')

print("A probabilidade é de :",norm.cdf(Z))