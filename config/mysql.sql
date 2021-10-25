FLUSH PRIVILEGES;

-- CREATE DATABASE
CREATE DATABASE IF NOT EXISTS library;

-- CREATE USER
CREATE USER IF NOT EXISTS 'pulpstack'@'localhost';

-- SET PASSWORD
-- https://dev.mysql.com/doc/refman/8.0/en/alter-user.html
ALTER USER 'pulpstack'@'localhost' IDENTIFIED BY "password";

-- GRANT ACCESS TO DATABASE
GRANT ALL ON library.* to 'pulpstack'@'localhost';

-- SHOW GRANTS
SHOW GRANTS FOR 'pulpstack'@'localhost';

FLUSH PRIVILEGES;
