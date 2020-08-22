import pandas as pd 

s = pd.Series(list('ahusahsuahsiihahsuia'))
print(s)

# Filtrando informações repetidas com o metodo .unique()
filtro = s.unique()
print(filtro)

# Verificando quantas vezes um dados se repetiu com o metodo .value_counts()
cont = s.value_counts()
print(cont)

# Tratando dados com os metodos .unique e .value_counts
dados = pd.read_csv('dados\\aluguel.csv', sep=';')
d1 = dados.Tipo.unique()                            # Nos apresenta todas os dados sem repetir da coluna Tipo
print(d1)

d2 = dados.Tipo.value_counts()                      # Nos apresenta uma seleção de frequencia pronta
print(d2)

