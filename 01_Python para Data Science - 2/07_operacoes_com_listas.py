# x in A
'''Verificando se um valor está contido em uma lista ou não.'''
acessorios = ['Rodas de liga', 'Trava elétrica', 'Piloto Automático', 'Banco de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
print(acessorios)

if 'Rodas de liga' in acessorios:
    print("True")
else:
    print("False")

if 'Rodas de liga' not in acessorios:
    print("True")
else:
    print("False")

if '4 X 4' in acessorios:
    print("True")
else:
    print("False")


# A + B
'''Concatenando duas listas.'''
A = ['Rodas de liga', 'Trava elétrica', 'Piloto Automático', 'Banco de couro']
B = ['Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']

print(A+B)

# len(A)
''' Verificando o tamanho de uma lista.'''
print(len(acessorios))