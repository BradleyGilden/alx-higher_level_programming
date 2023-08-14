# Structured Query Language (SQL)

SQL is a programming language for interacting with relational databases. This repository contains
the basic concepts and commands dealing with MySQL databases

## Directory 

* [0-list_databases.sql](0-list_databases.sql) - script lists all databases in sql server
* [1-create_database_if_missing.sql](1-create_database_if_missing.sql) - a script that creates the database hbtn_0c_0 in my MySQL server
* [2-remove_database.sql](2-remove_database.sql) - a script that deletes the database hbtn_0c_0 in my MySQL server
* [3-list_tables.sql](3-list_tables.sql) - a script that lists all the tables of a database in your MySQL server.
* [4-first_table.sql](4-first_table.sql) - a script that creates a table called first_table in the current database in your MySQL server
* [5-full_table.sql](5-full_table.sql) - a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
* [6-list_values.sql](6-list_values.sql) - a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
* []() -
* []() -
* []() -
* []() -
* []() -
* []() -
* []() -

<hr>

## Three types of SQL statements

### 1. Data Definition Language(DDL):
* Commands modify actual structure of a database, example:
  * Generating a table
  * Modifying table structure

### 2. Data Control Language(DCL):
* Commands manipulate/manage user access rights, consists of 2 commands:
  * GRANT : add database permissions for user
  * REVOKE: remove existing permissions

### 3. Data Manipulation Language(DML):
* Most frequently used SQL commands
* Used for searching, inserting, updating, and deleting data

### Note:
* SQL is case INSENSITIVE
* SQL statements can span over multiple lines and end with a semicolon `;`
