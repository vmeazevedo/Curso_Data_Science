import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model

# Importando a base de dados
passageiros = pd.read_csv('data\\Passageiros.csv', sep=',')
print(passageiros.head())

# Plotando um gráfico com as informações do dataframe
print(sns.lineplot(x='tempo',y='nPassageiros',data=passageiros))
plt.show()

''' Regressão Linear '''
# Selecionando somente os valores das colunas
Tempo = passageiros.iloc[:,:-1].values
nPassageiros = passageiros.iloc[:,:1].values

Tempo_treino, Tempo_teste, nPassageiros_treino, nPassageiros_teste = train_test_split(Tempo, nPassageiros, test_size = 0.3)

regressor = linear_model.LinearRegression()

regressor.fit(Tempo_treino, nPassageiros_treino)

nPassageiros_predito = regressor.predict(Tempo_teste)