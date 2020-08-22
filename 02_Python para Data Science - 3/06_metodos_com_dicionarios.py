dados = {'Jetta Variant': 88078.64, 'Crossfox': 72832.16, 'DS5': 124549.07}

# dict.update()
'''Atualiza o dicionario'''
dados.update({'Passat': 106161.94})
print(dados)

dados.update({'Passat': 106161.95, 'Fusca': 150000})    # Atualizamos o valor do Passat e incluimos o Fusca
print(dados)


# dict.copy()
'''Cria uma copia do dicionario'''
dadosCopy = dados.copy()
print(dadosCopy)
del dadosCopy['Fusca']
print(dadosCopy)
print(dados)

# dict.pop(key[, default])
'''Se a chave for encontrada no dicionario, o item é removido e seu valor é retornado. Caso contrário, o valor especificado como default é retornado. Se o valor default não for fornecido e a chave não for encontrada no dicionário um erro será gerado.'''
print(dadosCopy.pop('Passat'))
print(dadosCopy.pop('Passat', 'Chave não encontrada'))

# dict.clear()
'''Remove todos os itens do dicionario'''
dadosCopy.clear()
print(dadosCopy)