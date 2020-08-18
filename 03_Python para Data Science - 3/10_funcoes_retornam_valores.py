def media(lista):
    valor = sum(lista) / len(lista)
    return valor

resultado = media([1,2,3,4,5,6,7,8,9])
print(resultado)


# Função que retorna mais de um valor
def media(lista):
    valor = sum(lista) / len(lista)
    return (valor, len(lista))

print(media([1,2,3,4,5,6,7,8,9]))   # Retorna o valor da media e o comprimento da lista

# Desacoplamento 
def media(lista):
    valor = sum(lista) / len(lista)
    return (valor, len(lista))

resultado, n = media([1,2,3,4,5,6,7,8,9])   # Retorna o valor da media e o comprimento da lista em variaveis distintas
print(resultado)
print(n)

