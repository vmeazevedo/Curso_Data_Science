import pandas as pd 
import matplotlib.pyplot as plt 

plt.rc('figure', figsize = (14,6))

dados = pd.read_csv('01_Exercicios\\aluguel_amostra.csv',sep=';')
print(dados)

# Criando nossas estatisticas
valor = dados['Valor m2']
Q1 = valor.quantile(.25)
print(Q1)
Q3 = valor.quantile(.75)
print(Q3)
IQQ = (Q3 - Q1).round(2)
print(IQQ)
limite_inferior = (Q1 - 1.5 * IQQ).round(2)
print(limite_inferior)
limite_superior = (Q3 + 1.5 * IQQ).round(2)
print(limite_superior)

# Realizando uma seleção  com os valores de nossa estatistica
selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_new = dados[selecao]
dados_new.boxplot(['Valor m2'])
plt.show()