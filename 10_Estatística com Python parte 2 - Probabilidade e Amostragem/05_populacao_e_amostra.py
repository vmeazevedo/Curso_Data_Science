import pandas as pd 
import numpy as np
from scipy.special import comb
from scipy.stats import binom

# Importando nossa base
dados = pd.read_csv('data\\dados.csv',sep=',')


'''
- População 
Conjunto de todos os elementos de interesse em um estudo. Diversos elementos podem compor uma população, por exemplo: pessoas,
idades, alturas, carros, etc.
Com relação ao tamanho, as populaçoes podem ser limitadas (populações finitas) ou ilimitadas (populações inifinitas).

Populações finitas
Permitem a contagem de seus elementos. Como exemplos temos o numero de funcionario de uma empresa, a quantidade de alunos em uma escola.

Populações infinitas
Não é possível contar seus elementos. Como exemplos temos a quantidade de porções que se pode extrair da agua do mar para uma analise, temperatura medida em
cada ponto de um territorio, etc.

- Amostra
Subconjunto representativo da população

Os atributos numericos de uma população como sua média, variancia e desvio padrão, são conhecidos como parametros.
O principal foco da inferencia estatistica é justamente gerar estimativas e testar hipoteses sobre os parametros populacionais utilizando informações e amostras.'''


# Quando utilizar uma amostra?

''' 
- Populações infinitas
O estudo não chegaria nunca ao fim. Não é possível investigar todos os elementos da população.

- Testes destrutivos
Estudos onde os elementos avaliados são totalmente consumidos ou destruídos. Exemplo: testes de vida útil, teste de segurança contra colisões em automóveis.

- Resultados rápidos
Pesquisas que precisam de mais agilidade na divulgação. Exemplo: pesquisas de opinião, pesquisas que envolvam problemas de saude publica.

- Custos elevados
Quando a população é finita mas muito numero, o custo de um censo pode tornar o processo inviavel.
'''


'''
Amostragem Aleatória Simples
É uma das principais maneiras de se extrair uma amostra de uma população. A exigência fundamental deste tipo de abordagem é que cada elemento da população
tenha as mesmas chances de ser selecionado para fazer parte da amostra.
'''
# Apresentando informações basicas
print(dados.shape[0])
print(dados.Renda.mean())

# Pegando os mesmos dados de uma amostra de teste
amostra = dados.sample(n = 100, random_state = 101)
print(amostra.shape[0])
print(amostra.Renda.mean())

# Batendo as informações entre o dataset e a amostra
print(dados.Sexo.value_counts(normalize = True))
print(amostra.Sexo.value_counts(normalize = True))


''' 
Amostragem Estratificada
É uma melhoria do processo de amostragem aleatoria simples. Neste metodo é proposta a divisão da população em subgrupos de elementos com caracteristicas similares,
ou seja, grupos mais homogeneos. Com estes subgrupoos separados, aplica-se a técnica de amostragem aleatoria simples dentro de cada subgrupo individualmente.

Amostragem por Conglomerados
Tambem visa melhorar o critério de amostragem aleatoria simples. Na amostragem por conglomerados são também criados subgrupos, porém não será homogeneos como na 
amostragem estratificadas.'''