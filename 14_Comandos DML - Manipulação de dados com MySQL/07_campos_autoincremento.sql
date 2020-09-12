create table tab_identity (
id int auto_increment, 
descritor varchar(20),
primary key (id));

insert into tab_identity (descritor) values ('cliente1');
insert into tab_identity (descritor) values ('cliente2');
insert into tab_identity (descritor) values ('cliente3');
select * from tab_identity;

delete from tab_identity where id = 2;