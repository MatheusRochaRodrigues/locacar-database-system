create database Locadora;

use locadora;

create table cliente (
	id int auto_increment,
    nome varchar(50),
    telefone bigint,
    primary key (id)
);

create table carro (
	id int auto_increment,
	tipo varchar(30),
    diaria numeric(10,2),
	semanal numeric(10,2),
    marca varchar(30),
    modelo varchar(30),
    ano int,
    primary key(id)
);

create table aluga(
	Data_init date,
    id_carro_fk int,
    numeroDias int,
    ativo boolean,
    finalizado boolean,
    inAberto boolean,
    id_cliente_fk int,
    foreign key (id_carro_fk) references carro(id),
    foreign key (id_cliente_fk) references cliente(id),
    primary key (Data_Init, id_carro_fk)
);