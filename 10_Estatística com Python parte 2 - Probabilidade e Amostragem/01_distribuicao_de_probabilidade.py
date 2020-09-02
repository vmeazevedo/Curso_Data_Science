import pandas as pd 
from scipy.special import comb
from scipy.stats import binom

# Importando nossa base
dados = pd.read_csv('data\\dados.csv',sep=',')

'''Distribuição Binominal 
1 - Realização de n ensaios identicos
2 - Os ensaios são independentes
3 - Somente dois resultados são possíveis
4 - A probabilidade de sucesso é representada por p e a de fracasso por 1 - p = q. Estas probabilidades não se modificam de ensaio para ensaio.


Problema
Em um concurso para preencher uma vaga de cientista de dados temos um total de 10 questões de multiplas escolha com 3
alternativas possíveis em cada questão. Cada questão tem o mesmo valor. Suponha que um candidato resolva se aventurar sem ter
estudado absolutamente nada. Ele resolver fazer a prova de olhos vendados e chutar todas as respostas. Assumindo que a prova vale
10 pontos e a nota de corte seja 5, obtenha a probabilidade deste candidato acertar 5 questões e também a probabilidade deste
candidato passar para a próxima etapa do processo seletivo.
'''

# Qual o numero de ensaios (n)?
n = 10
print(f'n é igual = {n}')
# Os ensaios são independentes?
'''Sim. A opção escolhida em uma questão não influencia a próxima'''
# Somente dois resultados são possíveis em cada ensaio?
'''Sim. O candidato tem duas possibilidades, certo ou errado em uma questão.'''
# Qual a probabilidade de sucesso (p)?
numero_de_alternativas_por_questao = 3
p = 1 / numero_de_alternativas_por_questao
print(f'p é igual = {p}')
# Qual a probabilidade de fracasso (q)?
q = 1 - p
print(f'q é igual = {q}')
# Qual o total de eventos que se deseja obter sucesso (k)?
k = 5 
print(f'k é igual = {k}')

'''Solução 1'''
# Na mão
probabilidade = (comb(n,k) * (p ** k) * (q ** (n - k)))
print('Probabilidade = %0.8f' % (probabilidade*100) + '%')

'''Solução 2'''
# Com Python
probabilidade = binom.pmf(k,n,p)
print('Probabilidade = %0.8f' % (probabilidade*100) + '%')



''' Obter a probabilidade do candidato passar '''
passar = binom.pmf([5,6,7,8,9,10],n,p).sum()
print(f'Probabilidade de passar = {passar*100} + %')