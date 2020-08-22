dados = {
    'Crossfox': {'km': 35000, 'ano': 2005},
    'DS5': {'km': 17000, 'ano': 2015},
    'Fusca': {'km': 130000, 'ano': 1979}
}

def km_media(dataset, ano_atual):
    '''Imprime a km media anual de cada veiculo do dicionario'''
    for item in dataset.items():
        result = item[1]['km'] / (ano_atual - item[1]['ano'])
        print(result)

km_media(dados, 2019)