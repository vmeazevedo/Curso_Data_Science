import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

gorjetas = pd.read_csv('data\\tips_tratados.csv',sep=',')
print(gorjetas.head())

''' Analise 1 - Valor da conta e gorjetas '''
print(gorjetas.columns)

# Gerando um gráfico scatterplot, comparativo entre o eixo x e y
valor_gorjeta = sns.scatterplot(x='valor_da_conta', y='gorjeta', data=gorjetas)
plt.title("Visulamente o valor da gojeta aumenta conforme o valor da conta")
plt.show()          # Visulamente o valor da gojeta aumenta conforme o valor da conta

# Verificando se temos registros nulos em nossa base
s = gorjetas.shape[0]
print(f"\nA base de dados contém {s} registro.")
print("\nRegistros não nulos\n", gorjetas.count())


''' Criando o campo porcentagem '''
gorjetas['porcentagem'] = gorjetas['gorjeta'] / gorjetas['valor_da_conta']
gorjetas.porcentagem = gorjetas.porcentagem.round(2)
print(gorjetas.head())  

# Gerando um gráfico scatterplot, comparativo entre o eixo x e y
porcentagem_conta = sns.scatterplot(x='valor_da_conta', y='porcentagem', data=gorjetas)
plt.title("Visualmente o valor da conta não é proporcional ao valor da gorjeta")
plt.show()          # Visualmente o valor da conta não é proporcional ao valor da gorjeta


# Apresentando o grafico anterior em linha
porcentagem_conta_linha = sns.relplot(x='valor_da_conta', y='porcentagem', kind='line',data=gorjetas)
plt.show()
# Apresentando o grafico anterior demonstrando a queda
porcentagem_conta_linha = sns.lmplot(x='valor_da_conta', y='porcentagem',data=gorjetas)
plt.show()

# Exportando nosso novo DataFrame
gorjetas.to_csv('data\\tips_tratados_2.csv', sep=',', index=False)