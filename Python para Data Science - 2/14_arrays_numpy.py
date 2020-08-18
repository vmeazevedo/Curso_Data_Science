import numpy as np

# Criando um array com dados aleatorios
km = np.array([1000, 2330, 4897, 1500])
print(km)
print(type(km))

# Criando um array com dados importados
km = np.loadtxt(fname = 'data\\carros-km.txt', dtype = int)
print(km)
print(km.shape)   # mostra a quantidade de elementos

# Criando um array a partir de uma lista de listas
dados = [
    ['Rodas de liga', 'Trava elétrica', 'Piloto Automático', 'Banco de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimidia', 'Teto panoramico', 'Freio ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automatico', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automatico', 'Bancos de couro', 'Central multimídia', 'Vidros eletricos']]

acessorios = np.array(dados)
print(acessorios)
print(acessorios.shape)

# Comparando desempenho com listas
np_array = np.arange(1000000)