import pandas as pd

# Importando nossa base e lendo o dataset do projeot
dados = pd.read_csv('data\\dados.csv',sep=',')
print(dados.head())


''' Tipos de Dados
- Variáveis qualitativas ordinais
    Variáveis que podem ser ordenadas ou hierarquizadas '''

print(sorted(dados['Anos de Estudo'].unique()))

'''
- Variáveis qualitativas nominais
    Variáveis que não podem ser ordenadas ou hierarquizadas '''

print(sorted(dados['UF'].unique()))
print(sorted(dados['Sexo'].unique()))
print(sorted(dados['Cor'].unique()))

'''
- Variáveis quantitativas discretas
    Variáveis que representam uma contagem onde os valores possíveis formam um conjunto finito ou enumerável '''

print(f"De {dados.Idade.min()} até {dados.Idade.max()} anos")

# Observação:
# A variável idade pode ser classificada de três formas distintas:
# 1 - Quantitativa discreta - quando representas anos completos (números inteiros);
# 2 - Quantitativa contínua - quando representa a idade exata, sendo representado por frações de anos;
# 3 - Quantitativa ordinal - quando representa faixas de idade.

'''
- Variável quantitativa contínuas
    Variáveis que representam uma contagem ou mensuração que assumem valores em uma escala contínua (números reais) '''

print(f"De {dados.Altura.min()} até {dados.Altura.max()} metros")