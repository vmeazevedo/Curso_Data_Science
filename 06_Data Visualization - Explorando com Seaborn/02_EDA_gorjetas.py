import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

gorjetas = pd.read_csv('data\\tips_tratados_2.csv',sep=',')


''' Análise 2 - Sobremesa '''
# Filtrando somente um campo em uma coluna
print(gorjetas[gorjetas.sobremesa=='Sim'])

# Dados das pessoas que pediram sobremesa
print(gorjetas[gorjetas.sobremesa=='Sim'].describe().round(3))

# Dados das pessoas que não pediram sobremesa
print(gorjetas[gorjetas.sobremesa=='Não'].describe().round(3))

# Analisando a realação sobremesa x gorjeta
sns.catplot(x='sobremesa',y='gorjeta',data=gorjetas)
plt.show()

# Analisando melhor a relação valor da conta x gorjeta
# lmplot plota um grafico com linha melhorando a visualização da tendencia
# hue = muda a cor para cada item da coluna informada
# col = separa em varias colunas, como temos só dois itens separou em 2 colunas
sns.lmplot(x='valor_da_conta',y='gorjeta', col='sobremesa', hue='sobremesa', data=gorjetas)
plt.show()

# Analisando melhor a relação valor da conta x porcentagem
sns.lmplot(x='valor_da_conta',y='porcentagem', col='sobremesa', hue='sobremesa', data=gorjetas)
plt.show()

''' Visualmente existe uma diferença no valor da gorjeta daqueles que pediram sobremesa e daqueles que não pediram '''

# Exportando nosso novo DataFrame
gorjetas.to_csv('data\\tips_tratados_3.csv', sep=',', index=False)