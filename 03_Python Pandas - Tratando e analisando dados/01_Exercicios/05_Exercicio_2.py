'''
Suponha que estejamos testando as moedas que serão utilizadas por árbitros de futebol
nas competições da Copa do Mundo. Atualmente, estas moedas são personalizadas e utilizadas 
em certos momentos dos jogos para decidir, na sorte, uma disputa. Nosso objetivo é verificar 
se as moedas que serão utilizadas nas competições não sejam viciadas.

Para isso testes foram realizados com cinco moedas e os resultados foram os seguintes:

Acima, temos o resultado de 50 lançamentos de cada moeda (m1, m2, m3, m4 e m5), 
onde c representa a ocorrência do evento CARA e C representa a ocorrência do evento COROA.

Para tirarmos nossas conclusões, precisamos montar o seguinte DataFrame:

Onde Freq. C e Freq. c são, respectivamente, as frequências de COROAS e de CARAS em cada teste.
'''
import pandas as pd 

m1 = 'CCcCCccCCCccCcCccCcCcCCCcCCcccCCcCcCcCcccCCcCcccCc'
m2 = 'CCCCCccCccCcCCCCccCccccCccCccCCcCccCcCcCCcCccCccCc'
m3 = 'CccCCccCcCCCCCCCCCCcccCccCCCCCCccCCCcccCCCcCCcccCC'
m4 = 'cCCccCCccCCccCCccccCcCcCcCcCcCcCCCCccccCCCcCCcCCCC'
m5 = 'CCCcCcCcCcCCCcCCcCcCCccCcCCcccCccCCcCcCcCcCcccccCc'

eventos = {'m1': list(m1), 
            'm2': list(m2), 
            'm3': list(m3), 
            'm4': list(m4), 
            'm5': list(m5)}

moedas = pd.DataFrame(eventos)

df = pd.DataFrame(data = ['Cara', 'Coroa'], index = ['c', 'C'], columns = ['Faces'])

for item in moedas:
    df = pd.concat([df, moedas[item].value_counts()], axis = 1)

print(df)