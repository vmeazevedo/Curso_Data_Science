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


''' Alucar - Analisando assinantes da newsletter '''

# Importando a base de dados
assinantes = pd.read_csv('data\\newsletter_alucar.csv',sep=',')
print(assinantes.head())

# Verificando o tipo de nossa base
print(assinantes.dtypes)

print("\nQuantidades de linhas e colunas:", assinantes.shape)
print("Quantidades de dados nulos:",assinantes.isna().sum().sum(),"\n")

# Convertendo a coluna mes de object para datetime
assinantes['mes'] = pd.to_datetime(assinantes['mes'])
print(assinantes.dtypes)

# Descobrindo o aumento do numero de assinantes e a aceleração
assinantes['aumento'] = assinantes['assinantes'].diff()
assinantes['aceleracao'] = assinantes['aumento'].diff()
print(assinantes.head())

# Plotando um gráfico mes x assinantes, aumento, aceleração
plot_comparacao('mes','assinantes','aumento','aceleracao',assinantes,'Análise de assinantes da newsletter')
