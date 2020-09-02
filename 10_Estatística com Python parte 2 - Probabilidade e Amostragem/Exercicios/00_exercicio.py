from scipy.special import comb

'''
Suponha que acabamos de criar um jogo de loteria, chamado Show de prêmios da Alura. 
Neste nosso novo jogo, o apostador marca 20 números, dentre os 25 disponíveis no bilhete, 
e pode ganhar até 1 milhão de reais.

Determine qual o número de combinações possíveis (espaço amostral) e a probabilidade de se 
ganhar o prêmio jogando apenas um bilhete (considere apenas quinze casas decimais).
'''

combinacoes = comb(25, 20)
probabilidade = 1 / combinacoes
print('Combinações = %d e Probabilidade = %0.15f' % (combinacoes, probabilidade))