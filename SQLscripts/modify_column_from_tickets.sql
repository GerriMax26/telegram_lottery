use lottery;
alter table tickets
modify column user_ticket int,
modify column win_ticket int;