create database clients;
use clients;

create table city(
    id int(3),
    name varchar(100),
    primary key (id)
)engine=InnoDB;

create table user(
    id int(10) not null,
    name varchar(100) not null,
    lastname varchar(100) not null,
    email varchar(100) not null unique,
    id_city int(3) not null unique,
    Primary key (id), 
    foreign key (id_city) references city(id)
) engine=InnoDB ;

CREATE TABLE phone_numbers (
    number varchar(12),
    id INT NOT NULL,
    KEY (id),
    FOREIGN KEY (id) REFERENCES user (id)
    ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

create table client (
    client_id int(10) PRIMARY KEY REFERENCES user (id),
    shippingQuantity int(3)
) engine=InnoDB;

CREATE TABLE addresses (
    address varchar(100),
    id INT NOT NULL,
    KEY (id),
    FOREIGN KEY (id) REFERENCES client (client_id)
    ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

insert into city values (0,"Bogota");
insert into city values (1,"Cali");
insert into user values (0,"Andres","Ramirez","andresramirez@gmail.com",0);
insert into user values (1,"Felipe","Hernandez","felipehernandez@gmail.com",1);
insert into phone_numbers values ("4562651",0);
insert into phone_numbers values ("4578951",0);
insert into phone_numbers values ("2131265",1);
insert into client values (0,3);
insert into client values (1,1);
insert into addresses values ("cra 1 # 1 - 1",0);
insert into addresses values ("cra 2 # 2 - 2",1);
insert into addresses values ("cra 3 # 3 - 3",1);

select u.id, concat(u.name," ",u.lastname) as name, u.email, c.name as city, p.number, cl.shippingQuantity, a.address from user u 
inner join city c on u.id_city=c.id 
inner join phone_numbers p on u.id=p.id
inner join client cl on u.id=cl.client_id
inner join addresses a on cl.client_id=a.id;