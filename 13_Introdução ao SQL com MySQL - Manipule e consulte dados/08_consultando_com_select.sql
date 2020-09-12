# Selecionando a base intente
SELECT * FROM tbcliente;
# Selecionando somente duas colunas
SELECT CPF, NOME FROM tbcliente;
# Selecionando apenas 5 registros de duas colunas
SELECT CPF, NOME FROM tbcliente LIMIT 5;
# Apresentando as colunas colocando um outro nome nelas
SELECT CPF AS CPF_CLIENTE, NOME AS NOME_CLIENTE FROM tbcliente;
