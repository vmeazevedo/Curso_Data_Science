import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

''' Alucar - Analisando as vendas '''

alucar = pd.read_csv('data\\alucar.csv',sep=',')
print(alucar.head())

# Verificando o tamanho da base
print("Quantidade de linhas e colunas:", alucar.shape)

# Verificando se temos valores nulos
print("Quantidade de dados nulos:",alucar.isna().sum().sum())

# Verificando o tipo das colunas
print(alucar.dtypes)

# Convertendo a coluna mês para datetime
alucar['mes'] = pd.to_datetime(alucar['mes'])
print(alucar.dtypes)

# Plotando um gráfico sobre as vendas do mês
sns.lineplot(x='mes',y='vendas',data=alucar)
plt.show()

''' Melhorando o nosso gráfico com o seaborn'''
# Utila a paleta de cores especifica do Accent
sns.set_palette('Accent')                   
# Coloca um grid no fundo escuro
sns.set_style('darkgrid')           
# Passamos os eixos do nosso grafico e a base de dados        
ax = sns.lineplot(x='mes',y='vendas',data=alucar)
# Aumenta a proporção do grafico
ax.figure.set_size_inches(12,6)             
# Setando um titulo no nosso gráfico, e informamos a posição do titulo e a fonte
ax.set_title("Vendas Alucar 2017 e 2018", loc='left', fontsize=18)
# Configurando os textos dos eixos x e y
ax.set_xlabel('Tempo', fontsize=14)
ax.set_ylabel('Vendas (R$)', fontsize=14)   
plt.show()


''' Verificando quanto aumentou por mês '''
# Utilizamos o metodo diff para subtrair o dados do mes seguinte pelo mes anterior, assim teremos a diferença
alucar['aumento'] = alucar['vendas'].diff()
print(alucar.head())

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

# Criando um gráfico com as informações do aumento
# Passando os dados a serem plotados
plotar('Aumento das vendas da Alucar de 2017 e 2018','Tempo','Aumento','mes','aumento',alucar)


''' Verificando a aceleração do crescimento da empresa '''
alucar['aceleracao'] = alucar['aumento'].diff()
print(alucar.head())

# Plotando o grafico de aceleração
plotar('Aceleração das vendas da Alucar de 2017 e 2018','Tempo','Aceleração','mes','aceleracao',alucar)



''' Unindo os 3 gráficos anteriores '''
# Configurando o tamanho do gráfico
plt.figure(figsize=(16,12))

# Utilizando o .subplot(x,x,x) para apresentar nossos gráficos
# 1º x = quantidade de graficos
# 2º x = a quantidade de grafico apresentada no eixo x
# 3º x = a posição/ordem do grafico
 
# Colocando o nosso grafico de mes x vendas como o inicial
ax = plt.subplot(3,1,1)
ax.set_title("Análise de vendas da Alucar de 2017 e 2018", fontsize=18, loc='left')
sns.lineplot(x='mes',y='vendas',data=alucar)

# Colocando o nosso grafico de mes x aumento como segundo
plt.subplot(3,1,2)
sns.lineplot(x='mes',y='aumento',data=alucar)

# Colocando o nosso grafico de mes x aceleração como terceiro
plt.subplot(3,1,3)
sns.lineplot(x='mes',y='aceleracao',data=alucar)
plt.show()

# Criando uma função para realizar o plot dos 3 gráficos
def plot_comparacao(x,y1,y2,y3,dataset,titulo):
    plt.figure(figsize=(16,12))
    ax = plt.subplot(3,1,1)
    ax.set_title(titulo, fontsize=18, loc='left')
    sns.lineplot(x=x,y=y1,data=dataset)
    plt.subplot(3,1,2)
    sns.lineplot(x=x,y=y2,data=dataset)
    plt.subplot(3,1,3)
    sns.lineplot(x=x,y=y3,data=dataset)
    plt.show()

# Plotando os 3 gráficos
plot_comparacao('mes','vendas','aumento','aceleracao',alucar,'Análise das Vendas da Alucar de 2017 e 2018')
