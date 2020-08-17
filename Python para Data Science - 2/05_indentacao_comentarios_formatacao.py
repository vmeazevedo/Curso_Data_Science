# Indentação
ano_atual = 2019
ano_fabricação = 2019

if (ano_atual == ano_fabricação):
    print("verdadeiro")
else:
    print("Falso")

# Comentários
# Isto é um comentário

# Isto
# é um
# comentário

'''
Isto é um comentário
'''


# Formatação de Strings
# str.format()
print("Olá, {}!".format("Vinicius"))
print("Olá, {}! Este é seu acesso de numero {}".format("Vinicius", 32))

# f-string
nome = 'Vinicius'
acessos = 32

print(f"Olá, {nome}!")
print(f"Olá, {nome}! Este é seu acesso de numero {acessos}")
