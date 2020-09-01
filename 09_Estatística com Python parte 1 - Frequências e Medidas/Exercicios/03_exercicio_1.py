import pandas as pd

dataset = pd.DataFrame({
    'Sexo': ['H', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'M', 'M'],
    'Idade': [53, 72, 54, 27, 30, 40, 58, 32, 44, 51]
})

'''
Observação: Na variável Sexo, 'H' representa os homens e 'M' as mulheres.

Assinale a alternativa que apresenta o valor do desvio padrão da variável Idade.
'''

print(dataset)

var_idade = dataset[['Idade']]
print(var_idade)

desvio_padrao = var_idade.std()
print(desvio_padrao)

# Metodo que eu fiz
var_idade2 = dataset.query("Sexo == 'M'")
print(var_idade2['Idade'].std())

# Resposta do exercicio
# dataset.groupby(['Sexo']).std().loc['M']