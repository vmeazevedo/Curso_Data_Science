# Selecionando todos os clientes que tem idade igual a 22
select * from tbcliente where idade = 22;
# Selecionando todos os clientes que tem idade maior e menor que 22
select * from tbcliente where idade > 22;
select * from tbcliente where idade < 22;
# Selecionando todos os clientes que tem idade menor igual a 22
select * from tbcliente where idade <= 22;
# Selecionando todos os clientes que tem idade diferente de 22
select * from tbcliente where idade <> 22;

# Selecionando um valor em float com o comando between
select * from tbproduto where preco_lista between 16.007 and 16.009;