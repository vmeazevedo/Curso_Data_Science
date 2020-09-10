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


