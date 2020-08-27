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


''' Chocolura - Analisando as vendas'''
# Importando o database
chocolura = pd.read_csv('data\\chocolura.csv',sep=',')
print(chocolura.head())

# Verificando o tipo
print(chocolura.dtypes)

# Alterando de object para datetime da data do mes
chocolura['mes'] = pd.to_datetime(chocolura['mes'])
print(chocolura.dtypes)

# Salvando informações de tamanho da base e qtd de nulos
print("Quantidade de linhas e colunas:", chocolura.shape)
print("Quantidades de dados nulos:", chocolura.isna().sum().sum())

# Usando metodo diff para pegar a diferença das vendas e dos aumentos
chocolura['aumento'] = chocolura['vendas'].diff()
chocolura['aceleracao'] = chocolura['aumento'].diff()
print(chocolura.head())

# Plotando as infoamações de vendas, aumento e aceleração x mes
plot_comparacao('mes','vendas','aumento','aceleracao',chocolura,'Análise de vendas da Chocolura de 2017 a 2018')

''' Identificamos um pico nos meses de abril e julho, que são respectivos a pascoa e dia dos namorados.'''


''' Statsmodels'''
# Importando o database
chocolura = pd.read_csv('data\\chocolura.csv',sep=',')
print(chocolura.head())

resultado = seasonal_decompose([chocolura['vendas']], freq=1)
plt.show()