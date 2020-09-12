create table tab_padrao (
id int auto_increment,
descrito varchar(20),
endereco varchar(100) null,
cidade varchar(50) default 'Rio de Janeiro',
data_criacao timestamp default current_timestamp(),
primary key (id));

insert into tab_padrao(descrito, endereco, cidade, data_criacao)
values ('clientex', 'rua x', 'são paulo', '2020-01-01');

select * from tab_padrao;

insert into tab_padrao(descrito)
values ('clientey');
