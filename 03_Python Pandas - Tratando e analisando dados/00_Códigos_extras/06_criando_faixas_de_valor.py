import pandas as pd 

dados = pd.read_csv('dados\\aluguel_residencial_3.csv', sep=';')
print(dados.head(10))

# 1 e 2
# 3 e 4
# 5 e 6
# 7 ou mais

classes = [0,2,4,6,100]

quartos = pd.cut(dados.Quartos, classes)            # A função cut() é uma ferramenta do pandas que auxilia na criação distribuições de frequências.
print(quartos)
print(pd.value_counts(quartos))

labels = ['1 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 quartos ou mais']
quartos = pd.cut(dados.Quartos, classes, labels= labels)
print(pd.value_counts(quartos))