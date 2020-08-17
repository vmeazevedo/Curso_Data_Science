idades = [18, 22, 15, 50]

def verifica_dirigir(idade):
    for idade in idades:
        if idade >= 18:
            print(f" {idade} anos de idade, TEM permissão para dirigir.")
        else:
            print(f" {idade} anos de idade, NÃO tem permissão para dirigir.")

verifica_dirigir(idades)