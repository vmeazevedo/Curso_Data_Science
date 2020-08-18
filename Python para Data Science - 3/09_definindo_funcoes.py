# Funções sem parametros
def media():
    valor = (1 + 2 + 3) / 3
    print(valor)

media()

# Funções com parametros
def media(number_1, number_2, number_3):
    valor = (number_1 + number_2 + number_3) / 3
    print(valor)

media(1,2,3)
media(23,45,67)

def media(lista):
    valor = sum(lista) / len(lista)
    print(valor)

media([1,2,3,4,5,6,7,8,9])