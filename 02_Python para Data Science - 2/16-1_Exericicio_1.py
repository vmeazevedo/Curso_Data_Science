import numpy as np

'''
Considere o seguinte array:
'''

dados = np.array(
    [
        ['Roberto', 'casado', 'masculino'],
        ['Sheila', 'solteiro', 'feminino'],
        ['Bruno', 'solteiro', 'masculino'],
        ['Rita', 'casado', 'feminino']
    ]
)

'''
Marque a alternativa que mostra o código que permite a seleção, sem utilização de operadores lógicos (and e or), das informações de nome e estado civil, somente das pessoas do sexo masculino.
'''

print(dados[0::2, :2])
