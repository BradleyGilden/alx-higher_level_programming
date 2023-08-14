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
* [7-insert_value.sql](7-insert_value.sql) - a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server
* [8-count_89.sql](8-count_89.sql) - a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server
* [9-full_creation.sql](9-full_creation.sql) - a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows
* [10-top_score.sql](10-top_score.sql) - a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
* [11-best_score.sql](11-best_score.sql) - a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
* [12-no_cheating.sql](12-no_cheating.sql) - a script that updates the score of Bob to 10 in the table second_table
* [13-change_class.sql](13-change_class.sql) - a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server
* [14-average.sql](14-average.sql) - a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server
* [15-groups.sql](15-groups.sql) - a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
* [16-no_link.sql](16-no_link.sql) - a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
* [100-move_to_utf8.sql](100-move_to_utf8.sql) - a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server
* [101-avg_temperatures.sql](101-avg_temperatures.sql) - a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
* [102-top_city.sql](102-top_city.sql) - a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
* [103-max_state.sql](103-max_state.sql) - a script that displays the max temperature of each state (ordered by State name)

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
