import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import autocorrelation_plot

# Criando uma função para realizar o plot do gráfico
def plotar(titulo,labelx, labely,x,y,dataset):
    sns.set_palette('Accent')                   
    sns.set_style('darkgrid')           
    ax = sns.lineplot(x=x,y=y,data=dataset)
    ax.figure.set_size_inches(12,6)             
    ax.set_title(titulo, loc='left', fontsize=18)
    ax.set_xlabel(labelx, fontsize=14)
    ax.set_ylabel(labely, fontsize=14)   
    plt.show()

# Criando uma função para realizar o plot dos 3 gráficos
def plot_comparacao(x,y1,y2,y3,dataset,titulo):
    sns.set_palette('Accent')                   
    sns.set_style('darkgrid') 
    plt.figure(figsize=(16,12))
    ax = plt.subplot(3,1,1)
    ax.set_title(titulo, fontsize=18, loc='left')
    sns.lineplot(x=x,y=y1,data=dataset)
    plt.subplot(3,1,2)
    sns.lineplot(x=x,y=y2,data=dataset)
    plt.subplot(3,1,3)
    sns.lineplot(x=x,y=y3,data=dataset)
    plt.show()


''' Cafelura - Analise de Vendas'''
# Importando o database
cafelura = pd.read_csv('data\\cafelura.csv',sep=',')
print(cafelura.head())

print("Quantidade de registros:", cafelura.shape)
print("Quantidade de dados nulos:", cafelura.isna().sum().sum())

print(cafelura.dtypes)
cafelura['mes'] = pd.to_datetime(cafelura['mes'])
print(cafelura.dtypes)

plotar("Vendas da Cafelura de 2017 e 2018",'Tempo','Vendas','mes','vendas',cafelura)


quantidade_de_dias_de_fds = pd.read_csv('data\\dias_final_de_semana.csv',sep=',')
print(quantidade_de_dias_de_fds.head())

quantidade_de_dias_de_fds['quantidade_de_dias'].values

cafelura['vendas_normalizadas'] = cafelura['vendas'] /  quantidade_de_dias_de_fds['quantidade_de_dias'].values
print(cafelura.head())

plotar("Vendas normalizadas da Cafelura de 2017 a 2019","Tempor","Vendas Normalizadas","mes","vendas_normalizadas",cafelura)

plt.figure(figsize=(12,6))
ax = plt.subplot(2,1,1)
ax.set_title("Vendas Cafelura 2017 e 2018", fontsize=18)
sns.lineplot(x='mes',y='vendas',data=cafelura)
ax = plt.subplot(2,1,2)
ax.set_title("Vendas Normalizadas Cafelura 2017 e 2018", fontsize=18)
sns.lineplot(x='mes',y='vendas_normalizadas',data=cafelura)
plt.show()