dados = [
    ['Rodas de liga', 'Trava elétrica', 'Piloto Automático', 'Banco de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimidia', 'Teto panoramico', 'Freio ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automatico', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automatico', 'Bancos de couro', 'Central multimídia', 'Vidros eletricos']]

print(dados)

# Acessando as listas dentro de dados
for lista in dados:
    print(lista)

# Acessando as listas e listando os itens de dentro de todas elas
for lista in dados:
    for item in lista:
        print(item)

# Populando uma lista vazia com os dados que estava em nossa lista dados.
acessorios = []

for lista in dados:
    for item in lista:
        acessorios.append(item)

print(acessorios)


# set()
''' Usamos o sorted para organizar a lista, o list para converter ela em lista e o set para eliminar os valores repetidos'''
print(sorted(list(set(acessorios))))

