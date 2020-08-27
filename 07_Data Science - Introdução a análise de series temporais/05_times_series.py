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


''' Chocolura - Vendas diárias (Outubro e Novembro)'''
# Importando o database
vendas_por_dia = pd.read_csv('data\\vendas_por_dia.csv',sep=',')
print(vendas_por_dia.head())

print("Quantidade de registros:", vendas_por_dia.shape)
print("Quantidade de dados nulos:", vendas_por_dia.isna().sum().sum())

print(vendas_por_dia.dtypes)
vendas_por_dia['dia'] = pd.to_datetime(vendas_por_dia['dia'])
print(vendas_por_dia.dtypes)

vendas_por_dia['aumento'] = vendas_por_dia['vendas'].diff()
vendas_por_dia['aceleracao'] = vendas_por_dia['aumento'].diff()
print(vendas_por_dia.head())

plot_comparacao('dia','vendas','aumento','aceleracao',vendas_por_dia,'Analise de Vendas por dia - Outubro e Novembro - Chocolura')


''' Analisando a sazonalidade '''
# Utilizando o metodo day_name para colocar o dia da semana
vendas_por_dia['dia_da_semana'] = vendas_por_dia['dia'].dt.day_name()
print(vendas_por_dia.head(7))

# Traduzindo os dias da semana
vendas_por_dia['dia_da_semana'].unique()
dias_traduzidos = {
    'Monday':'Segunda',
    'Tuesday':'Terça',
    'Wednesday':'Quarta',
    'Thursday':'Quinta',
    'Friday':'Sexta',
    'Saturday':'Sabado',
    'Sunday':'Domingo'
}

vendas_por_dia['dia_da_semana'] = vendas_por_dia['dia_da_semana'].map(dias_traduzidos)
print(vendas_por_dia.head(14))


''' Agrupando os dias '''
# Criando um agrupamento classificado pelo dia da semana, onde vamos apresentar venda, aumento e aceleracai
vendas_agrupadas = vendas_por_dia.groupby('dia_da_semana')['vendas','aumento','aceleracao'].mean().round()
print(vendas_agrupadas.head(7))



''' Correlação das vendas diárias '''
sns.set_palette('Accent')                   
sns.set_style('darkgrid')           
ax = plt.figure(figsize=(12,6))
ax.suptitle("Correlação das vendas diárias", fontsize=18, x=0.25, y=0.95)
autocorrelation_plot(vendas_por_dia['vendas'])
plt.show()
ax = plt.figure(figsize=(12,6))
ax.suptitle("Correlação do aumento das vendas diárias", fontsize=18, x=0.25, y=0.95)
autocorrelation_plot(vendas_por_dia['aumento'][1:])
plt.show()
ax = plt.figure(figsize=(12,6))
ax.suptitle("Correlação da aceleração das vendas diárias", fontsize=18, x=0.25, y=0.95)
autocorrelation_plot(vendas_por_dia['aceleracao'][2:])
plt.show()