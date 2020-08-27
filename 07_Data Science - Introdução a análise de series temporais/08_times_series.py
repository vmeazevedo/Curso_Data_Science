import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.seasonal import seasonal_decompose

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

''' Alucel - Análise de vendas'''
# Importando o database
alucel = pd.read_csv('data\\alucel.csv',sep=',')
print(alucel.head())

print(alucel.dtypes)
alucel['dia'] = pd.to_datetime(alucel['dia'])
print(alucel.dtypes)

print("Quantidade de registros:",alucel.shape)
print("Quantidade de dados nulos:", alucel.isna().sum().sum())

alucel['aumento'] = alucel['vendas'].diff()
alucel['aceleracao'] = alucel['aumento'].diff()
print(alucel.head())

plot_comparacao('dia','vendas','aumento','aceleracao',alucel,'Análise de Vendas da Alucel de Outubro e Novembro 2018')


''' Média móvel '''
# Utilizando o metodo .rolling para demonstrar a media movel das vendas
alucel['media_movel'] = alucel['vendas'].rolling(7).mean()
print(alucel.head(7))

plotar("Análise de Vendas com média móvel de 7 dias",'Tempor','Média Móvel','dia','media_movel',alucel)