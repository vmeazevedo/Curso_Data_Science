'''
Note que o tempo de alguns atletas não foi registrado por algum erro no processo de medição. 
Observando os dados e tendo um conhecimento prévio do desempenho de cada atleta, você, como 
cientista de dados, resolve que é razoável para este caso específico atribuir o tempo médio 
de todos os atletas aos dados faltantes. 
'''

import pandas as pd 

atletas = pd.DataFrame([['Marcos', 9.62], ['Pedro', None], ['João', 9.69], 
                        ['Beto', 9.72], ['Sandro', None], ['Denis', 9.69], 
                        ['Ary', None], ['Carlos', 9.74]], 
                        columns = ['Corredor', 'Melhor Tempo'])

print("\nRelação dos Atletas X Melhor Tempo:\n", atletas.head(10))

print("\n- Tratando os dados, atribuindo a media dos valores para os valores null:")
atletas.fillna(atletas.mean(), inplace=True)        # Add a media dos valores com o metodo mean(), ao valores null
print(atletas)
