use lottery;

create table jackpot
(
	id_jackpot int not null auto_increment,
    primary key(id_jackpot),
    id_user int,
    jackpot_size float,
    user_ticket int,
    foreign key (id_user) references users (id_user)
);