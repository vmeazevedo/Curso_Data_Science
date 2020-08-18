# A.sort()
acessorios = ['Rodas de liga', 'Trava elétrica', 'Piloto Automático', 'Banco de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
acessorios.sort()
print(acessorios)

# A.append(x)
acessorios.append('4 X 4')
print(acessorios)

# A.pop(i)
acessorios.pop()
print(acessorios)
acessorios.pop(3)
print(acessorios)

# A.copy()
acessorios_2 = acessorios.copy()    # acessorios[:] é a mesma coisa que usarmos o copy()
print(acessorios_2)
acessorios.append('4 X 4')
print(acessorios)
print(acessorios_2)


