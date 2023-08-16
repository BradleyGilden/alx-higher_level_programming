-- a script that creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- grant all privileges to user on the sever
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
