DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id`            int(11) NOT NULL AUTO_INCREMENT,
  `username`      varchar(255) DEFAULT NULL,
  `hashed_password`      varchar(255) DEFAULT NULL,
  `full_name`      varchar(255) NOT NULL,
  `email`    varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='users table';