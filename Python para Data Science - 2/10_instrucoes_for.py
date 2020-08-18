# Loops com listas
acessorios = ['Rodas de liga', 'Trava elétrica', 'Piloto Automático', 'Banco de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
for item in acessorios:
    print(item)

# List comprehensions
print(range(10))

print(list(range(10)))      #criando uma lista com range

for i in range(10):         # percorrendo um range com o loop for
    print(i**2)

quadrado = []
for i in range(10):         # percorrendo um loop e salvando ele em uma lista
    quadrado.append(i**2)

print(quadrado)

''' Modelos de List comprehensions'''
[i ** 2 for i in range(10)]

quadrado2 = []
[quadrado2.append(i**2) for i in range(10)]
print(quadrado2)


