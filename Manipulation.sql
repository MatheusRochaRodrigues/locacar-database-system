SELECT @@GLOBAL.transaction_isolation, @@transaction_isolation;

select * from carro;
select * from cliente;
select * from aluga;

drop table carro;
drop table cliente;
drop table aluga;


delete from cliente where id > 0;
delete from aluga where numeroDias > 0;
delete from carro where id > 0;