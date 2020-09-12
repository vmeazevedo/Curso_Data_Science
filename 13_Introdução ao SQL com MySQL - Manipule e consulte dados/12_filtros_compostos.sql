# Filtrando utilizando o and
select * from tbproduto where preco_lista >= 16.007 and preco_lista <=16.009;
# Filtrando utilizando o or
select * from tbproduto where preco_lista >= 16.007 or preco_lista <=16.009;
# Filtrando utilizando mais de uma variavel
select * from tbcliente where idade >= 18 and idade <= 22 and sexo='M';
# Filtrando utilizando o between
select * from tbcliente where year(data_nascimento) between 1992 and 2000;

