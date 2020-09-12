# Filtrando datas com o comando where simples
select * from tbcliente where data_nascimento = '1995-01-13';
select * from tbcliente where data_nascimento > '1995-01-13';
select * from tbcliente where data_nascimento <= '1995-01-13';
select * from tbcliente where data_nascimento <> '1995-01-13';

# Filtrando datas com o comando where e utilizando uma função para especificar ano/mes/dia
select * from tbcliente where year(data_nascimento) = 1995;
select * from tbcliente where month(data_nascimento) = 10;
select * from tbcliente where day(data_nascimento) = 5;