-- create a database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create table cities with a primary key id that is uniquely auto-generated,
-- name that can't be NULL and state_id that references the id of states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
	name VARCHAR(256) NOT NULL,
	state_id INT NOT NULL,
	FOREIGN KEY (`state_id`) REFERENCES hbtn_0d_usa.states(`id`)
);
