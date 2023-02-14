use lottery;
DROP TABLE IF EXISTS `buy_tickets`;
CREATE TABLE `buy_tickets` (
  `id_ticket` int NOT NULL,
  PRIMARY KEY (`id_ticket`),
  `id_user` int,
  foreign key (`id_user`) references users (id_user)
)

