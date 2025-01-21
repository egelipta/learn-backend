DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `full_name` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `update_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='users table';

BEGIN;
INSERT INTO `users` (`id`, `username`, `password`, `full_name`, `email`,`create_time`, `update_time`) VALUES
(1, 'root', '$pbkdf2-sha256$29000$FwJAyNk7p1RKaS1F6B3jfA$wHI4F6/RCOX.cW8tY6Kqzx3dXSCjECFmivDdKGA41oY', 'Super Admin', 'root@mail.com', '2025-01-20 14:53:40.966951', '2025-01-20 07:54:52.020422');
COMMIT;
