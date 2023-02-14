use lottery;
DROP TABLE IF EXISTS `prize`;
CREATE TABLE `prize` (
  `id_prize`  int NOT NULL,
  PRIMARY KEY (`id_prize`),
  `amount_priz` float not null,
  `id_user` int,
  `id_buy_tickets` int,
  `id_buy_tickets_users` int,
  foreign key (`id_user`) references users (id_user),
  foreign key (`id_buy_tickets`) references buy_tickets (id_ticket),
  foreign key (`id_buy_tickets_users`) references buy_tickets (id_user)
);