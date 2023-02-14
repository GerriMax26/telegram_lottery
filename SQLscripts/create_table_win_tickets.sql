use lottery;
DROP TABLE IF EXISTS `win_tickets`;
CREATE TABLE `win_tickets` (
  `id_win_ticket` int NOT NULL,
  PRIMARY KEY (`id_win_ticket`),
  `id_user` int,
  `id_ticket` int,
  foreign key (`id_user`) references users (id_user),
  foreign key (`id_ticket`) references buy_tickets (id_ticket)
)

