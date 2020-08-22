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


''' Identificando e Removendo Outliners '''
dados.boxplot(['Valor'], by = ['Tipo'])
plt.show()

grupo_tipo = dados.groupby('Tipo')['Valor']

# Criando nossas estatisticas
Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IQQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQQ
limite_superior = Q3 + 1.5 * IQQ

dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])

dados_new.boxplot(['Valor'], by = ['Tipo'])
plt.show()

dados_new.to_csv('dados\\aluguel_residencial_sem_outliers.csv',sep=';')