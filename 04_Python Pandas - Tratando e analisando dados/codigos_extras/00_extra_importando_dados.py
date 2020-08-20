import pandas as pd 

''' JSON '''
# Importando dados json
json = open('extras\\dados\\aluguel.json')
print(json.read())

# Apresentando dados json em um dataframe
df_json = pd.read_json('extras\\dados\\aluguel.json')
print(df_json)

''' TXT '''
# Importando dados txt
txt = open('extras\\dados\\aluguel.txt')
print(txt.read())

# Apresentando dados txt em um dataframe
df_txt = pd.read_table('extras\\dados\\aluguel.txt')
print(df_txt)

''' EXCEL '''
# Apresentando dados excel em um dataframe
df_xlsx = pd.read_excel('extras\\dados\\aluguel.xlsx')
print(df_xlsx)

''' HTML '''
# Apresentando dados html em um dataframe
df_html = pd.read_html('extras\\dados\\dados_html_1.html')
print(df_html[0])


print("Acessando novo site:")
df_html = pd.read_html('extras\\dados\\dados_html_2.html')
tb = len(df_html)                                               # Verificando a quantidade de tabelas no site
print("Nos temos nesse site " + str(tb) + " tabelas")
print(df_html[1])                                                # Alterando o indice dentro do [] podemos acessar as 3 tabelas