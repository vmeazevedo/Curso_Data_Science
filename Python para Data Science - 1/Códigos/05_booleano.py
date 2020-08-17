permissoes = []
idades = [20,14,40]

def verificar_dirigir(idades, permissoes):
    for idade in idades:
        if idade >= 18:
            permissoes.append(True)
        else:
            permissoes.append(False)

verificar_dirigir(idades, permissoes)

print(permissoes)

for permissao in permissoes:
    if permissao == True:
        print("Tem permissão para dirigir.")
    else:
        print("Não tem permissão para dirigir.")