use vendas_sucos;

create table itens_notas (
numero varchar(5) not null,
codigo varchar(10) not null,
quantidade int,
preco float,
primary key (numero, codigo));

alter table itens_notas add constraint fk_notas
foreign key (numero) references notas (numero);

alter table itens_notas add constraint fk_produto
foreign key (codigo) references produtos (codigo);
