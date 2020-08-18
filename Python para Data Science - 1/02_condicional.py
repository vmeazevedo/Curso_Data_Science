idade = 20

def verifica_dirigir(idade_pessoa):
    if idade >= 18:
        print("Tem permissão para dirigir.")
    else:
        print("Não tem permissão para dirigir.")


def verificar_dirigir_sem_parametros():
    idade = int(input("Qual a sua idade? "))
    if idade >= 18:
        print("Tem permissão para dirigir.")
    else:
        print("Não tem permissão para dirigir.")

verificar_dirigir_sem_parametros()
# verifica_dirigir(idade)