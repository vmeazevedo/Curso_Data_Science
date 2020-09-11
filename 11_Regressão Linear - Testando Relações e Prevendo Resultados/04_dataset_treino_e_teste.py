import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

''' 
Estimando um Modelo de Regressão Linear para o Consumo

Regressão Linear
A analise de regressão diz respeito ao estudo da dependência de uma variável (a variável dependente) em relação a uma ou mais variáveis,
as variáveis explanatórias, visando estimar e/ou prever o valor médio da primeira em termos dos valores conhecidos ou fixados das segundas.
'''
# Leitura dos dados
dados = pd.read_csv('Dados/Consumo_cerveja.csv',sep=';')

# Importando do scikit-learn o train_test_split
from sklearn.model_selection import train_test_split

# Criando uma series para armazenar o consumo de cerveja (y)
y = dados['consumo']

# Criando um DataFrame para armazenar as variáveis explicativas (X)
X = dados[['temp_max','chuva','fds']]

# Criando os datasets de treino e de teste
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=2811)
# X_test, y_test = train_test_split(X,y, test_size=0.3, random_state=28)

# Verificando os tamanhos dos arquivos geraos pela função train_test_split
print(X_train.shape)
print(X_test.shape)

# Importando LinearRegression e metrics da biblioteca scikit-learn
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Instanciando a classe LinearRegression()
modelo = LinearRegression()

# Utilizando o método fit() do objeto "modelo" para estimar nosso modelo linear utilizando dados de TREINO (y_train, e X_train)
modelo.fit(X_train, y_train)

# Obtendo o coeficiente de determinação (R²) do modelo estimado com os dados de TREINO
''' O coeficiente de determinação é uma medida resumida que diz quanto a linha de regressão ajusta-se aos dados. É um valor entre 0 e 1. '''
print('R² = {}'.format(modelo.score(X_train, y_train).round(2)))

# Gerando previsões para os dados de TESTE (X_test) utilizando o método predict() do objeto 'modelo'
y_previsto = modelo.predict(X_test)

# Obtendo o coeficiente de determinação para as previsões do nosso modelo.
print('R² = %s' % metrics.r2_score(y_test, y_previsto).round(2))


'''
Obtendo Previsões Pontuais
'''
# Dados de Entrada
entrada = X_test[0:1]
print(entrada)

# Gerando previsão pontual
modelo.predict(entrada)[0]

# Criando um simulador simples
temp_max = 30.5
chuva = 12.2
fds = 0
entrada=[[temp_max, chuva, fds]]

print('{0:.2f} litros'.format(modelo.predict(entrada)[0]))
print('\n')


'''
Interpretação dos Coeficientes Estimados
'''
# Obtendo o intercepto do modelo
''' O intercepto representa o efeito médio em Y (Consumo de Cerveja) tendo todas as variáveis explicativas excluídas do modelo.
De forma mais simples, o intercepto representa o efeito médio em Y (Consumo de Cerveja)  quando X2 (Temperatura Máxima),
X3 (Chuva) e X4 (Final de Semana) são iguais a zero.'''
print(modelo.intercept_)
print(type(modelo.intercept_))

# Obtendo os coeficientes de regressão
''' Os coeficientes de regressão B2,B3 e B4 são conhecidos como coeficientes parciais de resgressão ou coeficientes parciais angulares.
Considerando o número de variáveis explicativas de nosso modelo, seu significado seria o seguinte: B2 mede a variação no valor médio de Y,
por unidade de variação em X2, mantendo-se os valores de X3 e X4 constantes. Em outras palavras, ele nos dá o efeito "direto" ou "liquido"
de uma unidade de variação em X2 sobre o valor médio de Y, excluidos os efeitos que X3 e X4 possam ter sobre média de Y. De modo análogo podemos
interpretar os demais coeficientes de regressão.'''
print(modelo.coef_)
print(type(modelo.coef_))

# Confirmando a ordem das variaveis explicativas no DF
print(X.columns)

# Criando uma lista com os nomes das variaveis do modelo
index=['Intercepto','Temperatura Máxima','Chuva (mm)','Final de Semana']

# Criando um DF para armazenar os coeficientes do modelo
print(pd.DataFrame(data=np.append(modelo.intercept_, modelo.coef_), index=index, columns=['Parâmetros']))

''' 
Interpretação dos Coeficientes Estimados
Intercepto -> Excluindo o efeito das variáveis explicativas (X2 = X3 = X4 = 0) o efeito médio no consumo de cerveja seria de 5951,98L.
Temperatura Máxima (°C) -> Mantendo-se os valores de X3 e X4 constantes, o acréscimo de 1°C na Temperatura Máxima gera uma variação média no consumo de cerveja de 684,74L.
Chuva (mm) -> Mantendo-se os valores de X2 e X4 constantes, o acréscimo de 1mm de chuva gera uma variação média no consumo de cerveja de -60,78L.
Final de Semana -> Mantendo-se os valores de X2 e X3 constantes, o fato de o dia ser classificado como final de semana gera uma variação média no constumo de cerveja de 5401,08L.
'''

'''
Análise Gráficas das Previsões do Modelo
'''

# Gerando as previsões do modelo para os dados de treino
y_previsto_train = modelo.predict(X_train)

# Gráfico de dispersão entre valor estimado e valor real
ax = sns.scatterplot(x=y_previsto_train, y= y_train)
ax.figure.set_size_inches(12,6)
ax.set_title('Previsão x Real', fontsize = 16)
ax.set_xlabel('Consumo de Cerveja (litros) - Previsão', fontsize = 14 )
ax.set_ylabel('Consumo de Cerveja (litros) - Real', fontsize = 14 )
plt.show()

# Obtendo os resíduos
residuo = y_train - y_previsto_train

# Gráfico de dispersão entre valor estimado e resíduos
ax = sns.scatterplot(x=y_previsto_train, y= residuo, s=50)
ax.figure.set_size_inches(12,6)
ax.set_title('Previsão x Real', fontsize = 16)
ax.set_xlabel('Consumo de Cerveja (litros) - Previsão', fontsize = 14 )
ax.set_ylabel('Residuos ', fontsize = 14 )
plt.show()

# Plotando a distribuição de frenquencias dos residuos
ax = sns.distplot(residuo)
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição de Frequências dos Resíduos', fontsize = 16)
ax.set_xlabel('Litros', fontsize = 14 )
plt.show()