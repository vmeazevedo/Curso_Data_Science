import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Importando a base de dados
dados = pd.read_csv('data\\tips.csv',sep=',')
print(dados.head())

''' Tradução das Colunas '''
# Tradução dos campos da coluna
dados.columns = ['valor_da_conta', 'gorjeta','sobremesa','dia_da_semana', 'hora_do_dia', 'total_de_pessoas']
gorjetas = dados
print('\n',gorjetas.head())


''' Tradução das Linhas '''
# Alterando para portugues a coluna sobremesa
print(gorjetas.sobremesa.unique())              # Verificando os valores unicos

sim_nao = {             # Criando um dicionario para renomear os campos sobremesa
    'No' : 'Não',
    'Yes' : 'Sim'
}

gorjetas.sobremesa = gorjetas.sobremesa.map(sim_nao)
print('\n',gorjetas.head())


# Alterando para portugues a coluna dia da semana
print(gorjetas.dia_da_semana.unique())

dias = {              # Criando um dicionario para renomear os campos dia da semana
    'Sun' : 'Domingo',
    'Sat' : 'Sabado',
    'Thur' : 'Quinta',
    'Fri' : 'Sexta'
}

gorjetas.dia_da_semana = gorjetas.dia_da_semana.map(dias)
print('\n',gorjetas.head())


# Alterando para portugues a coluna hora do dia
print(gorjetas.hora_do_dia.unique())

hora = {
    'Dinner' : 'Jantar',
    'Lunch' : 'Almoço'
}

gorjetas.hora_do_dia = gorjetas.hora_do_dia.map(hora)
print('\n',gorjetas.head(244))


# Exportando nosso novo DataFrame
gorjetas.to_csv('data\\tips_tratados.csv', sep=',', index=False)