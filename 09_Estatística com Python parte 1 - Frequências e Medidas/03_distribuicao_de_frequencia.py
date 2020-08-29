import pandas as pd

# Importando nossa base e lendo o dataset do projeot
dados = pd.read_csv('data\\dados.csv',sep=',')
print(dados.head())

''' Distribuição de frequências para variáveis quantitativas '''

# Passo 1 - Especificar os limites de cada classe
'''
Utilizar a seguinte classificação:
A - Acima de 20 SM
B - De 10 a 20 SM
C - De 4 a 10 SM
D - De 2 a 4 SM
E - Até 2 SM

onde SM é o valor do salário mínimo na época. Em nosso caso R$ 788,00 (2015)
A - Acima de 15.760
B - De 7.880 a 15.760
C - De 3.152 a 7.880 SM
D - De 1.576 a 3.152 SM
E - Até 1.576 SM
'''

min = dados.Renda.min()
max = dados.Renda.max()
print(f"\nO menor salario é {min}, e o maior é {max}")

classes = [0, 1576, 3152, 7880, 15760, 200000]
labels = ['E','D','C','B','A']


# Passo 2 - Criar a tabela de frequências

# Utilizamos o metodo cut para separar os dados das classes com as labels
# Depois usamos o value counts para agrupar as informações
print("\n Divisão dos entrevistados por classe social")
frequencia = pd.value_counts(
    pd.cut(
        x = dados.Renda, 
        bins = classes, 
        labels = labels, 
        include_lowest=True)
)
percentual = pd.value_counts(
    pd.cut(
        x = dados.Renda, 
        bins = classes, 
        labels = labels, 
        include_lowest=True),
        normalize=True
)

# Criando um novo DataFrame com as variaveis
dist_freq_quantitativa_personalidas = pd.DataFrame(
    {'Frequência': frequencia,
     'Porcentagem (%)': (percentual*100).round(2)})
print(dist_freq_quantitativa_personalidas.sort_index(ascending=False))
