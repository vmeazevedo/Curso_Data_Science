''' Relatório de Análise VIII
Identificando e Removendo Outliners '''

import pandas as pd 
import matplotlib.pyplot as plt 

plt.rc('figure', figsize = (14,6))

dados = pd.read_csv('dados\\aluguel_residencial_3.csv',sep=';')

# Realiando um boxplot para visualizarmos as estatisticas e ver os pontos que estão sendo os outliners
# dados.boxplot(['Valor'])
# plt.show()

# Verificando os dados maiores de 500000
d = dados[dados['Valor'] >= 500000]
print(d)

# Criando nossas estatisticas
valor = dados['Valor']
Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)
IQQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQQ
limite_superior = Q3 + 1.5 * IQQ

# Realizando uma seleção  com os valores de nossa estatistica
selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_new = dados[selecao]
dados_new.boxplot(['Valor'])
plt.show()
