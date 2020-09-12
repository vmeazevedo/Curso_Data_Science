use vendas_sucos;

create table clientes (
cpf varchar(11) not null,
nome varchar(100) null,
endereco varchar(150) null,
bairro varchar(50) null,
cidade varchar(50) null,
estado varchar(50) null,
cep varchar(8) null,
data_nascimento date null,
idade int null,
sexo varchar(1) null,
limite_credito float null,
volume_compra float null,
primeria_compra bit(1) null,
primary key (cpf));
