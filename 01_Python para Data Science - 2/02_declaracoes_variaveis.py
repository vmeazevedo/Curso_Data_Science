#Operadores de atribuição
# =
ano_atual = 2019
ano_fabricacao = 2003
km_total = 44410.0

km_media = km_total / (ano_atual - ano_fabricacao)
print(km_media, "km")

# +=
ano_atual = 2019
ano_fabricacao = 2003
km_total = 44410.0

km_media = km_total / (ano_atual - ano_fabricacao)
km_total += km_media
print(km_total, "km")

# Declaração múltipla
ano_atual, ano_fabricacao, km_total = 2019, 2003, 44410.0
km_media = km_total / (ano_atual - ano_fabricacao)
print(km_media, "km")
