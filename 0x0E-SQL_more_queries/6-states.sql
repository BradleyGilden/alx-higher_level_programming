-- create a database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- set it as default schema
USE hbtn_0d_usa;
-- create table states with a primary key id that is auto-generated and
-- a column name that can't be NULL
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
