use vendas_sucos;

create table produtos (
codigo varchar(10) not null,
descritor varchar(100) null,
sabor varchar(50) null,
tamanho varchar(50) null,
embalagem varchar(50) null,
preco_lista float null,
primary key (codigo));

create table vendedores (
matricula varchar(5) not null,
nome varchar(100) null,
bairro varchar(50) null,
comissao float null,
data_admissao date null,
feria bit(1) null,
primary key (matricula));