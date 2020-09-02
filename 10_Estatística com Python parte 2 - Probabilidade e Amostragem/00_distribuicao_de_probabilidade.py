import pandas as pd 
from scipy.special import comb

# Importando nossa base

dados = pd.read_csv('data\\dados.csv',sep=',')
# print(dados.head())

'''
Distribuição Binominal 
Um evetno binomial é caracterizado pela possibilidade de ocorrência de apenas duas categorias. Estas categorias somandas
representam todo o espaço amostralo, sendo também mutuamente excludentes, ou seja, a ocorrência de uma implica na não 
ocorrência da outra.
Em análises estatísticas o uso mais comum da distribuição binomial é na solução de problemas que envolvem situações de
sucesso e fracasso
'''

''' 
Exemplo: Mega Sena
Em um volante de loteria da Mega Sena temos um total de 60 números para escolher. A aposta mínima é de seis numeros.
Você que é curioso resolve calcular a probabilidade de se acertar na Mega Sena com apenas um jogo. Para isso precisamos
saber quantas combinações de seis numeros podem ser formadas com 60 numeros disponíveis. '''

combinacoes = comb(60,6)
probabilidade = 1 / combinacoes
print('Combinações = %d e Probabilidade = %0.15f' % (combinacoes, probabilidade))