use lottery;
create table tickets
(
	id_ticket int not null auto_increment,
    primary key(id_ticket),
    user_ticket int not null,
    win_ticket int not null,
    prize float,
    id_user int,
    foreign key (id_user) references users (id_user)
);