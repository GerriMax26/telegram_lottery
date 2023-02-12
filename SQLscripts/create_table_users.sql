use lottery;

create table users
(
	id_user int primary key not null unique,
    fullName varchar(50) default null,
    country varchar(30) default null,
    city varchar(45) default null,
    address varchar(45) default null,
    postCode int default null,
    phone varchar(20) unique default null,
    email varchar(45) unique default null,
    fullNameTG text not null,
    lang varchar(2) not null default 'en'
);