import pandas as pd
import numpy as np

# Importando nossa base e lendo o dataset do projeot
dados = pd.read_csv('data\\dados.csv',sep=',')
print(dados.head())

''' Distribuição de frequências para variáveis quantitativas '''

# Passo 1 - Definindo o número de classes
# Regra de Sturges

n = dados.shape[0]
print(n)

k = 1 + (10/3) * np.log10(n)
print(k)

k = int(k.round(0))

# Passo 2 - Criar a tabela de frequencias

frequencia = pd.value_counts(
    pd.cut(
        x = dados.Renda,
        bins = 17,
        include_lowest=True
    ),
    sort = False
)

percentual = pd.value_counts(
    pd.cut(
        x = dados.Renda,
        bins = 17,
        include_lowest=True
    ),
    sort = False,
    normalize=True
)

print(frequencia,percentual)


# Criando um novo DataFrame com as variaveis
dist_freq_quantitativa_amplitudes_fixas = pd.DataFrame(
    {'Frequência': frequencia,
     'Porcentagem (%)': (percentual*100).round(2)})
print(dist_freq_quantitativa_amplitudes_fixas.sort_index(ascending=False))