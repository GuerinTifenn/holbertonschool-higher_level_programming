#!/bin/bash

echo "-- Script to list all databases
SHOW DATABASES;" > 0-list_databases.sql

echo "-- Script to create the database hbtn_0c_0 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;" > 1-create_database_if_missing.sql

echo "-- Script to delete the database hbtn_0c_0
DROP DATABASE IF EXISTS hbtn_0c_0;" > 2-remove_database.sql

echo "-- Script to list all tables in the given database
SHOW TABLES;" > 3-list_tables.sql

echo "-- Script to create a table called first_table
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);" > 4-first_table.sql

echo "-- Script to show the full description of the table first_table
SHOW CREATE TABLE first_table;" > 5-full_table.sql

echo "-- Script to list all rows in the table first_table
SELECT * FROM first_table;" > 6-list_values.sql

echo "-- Script to insert a new row in the table first_table
INSERT INTO first_table (id, name) VALUES (89, 'Best School');" > 7-insert_value.sql

echo "-- Script to count the number of records with id = 89 in the table first_table
SELECT COUNT(*) FROM first_table WHERE id = 89;" > 8-count_89.sql

echo "-- Script to create the table second_table and add multiple rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);" > 9-full_creation.sql

echo "-- Script to list all records of the table second_table ordered by score
SELECT score, name FROM second_table ORDER BY score DESC;" > 10-top_score.sql

echo "-- Script to list all records with a score >= 10 in the table second_table
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;" > 11-best_score.sql

echo "-- Script to update the score of Bob to 10 in the table second_table
UPDATE second_table SET score = 10 WHERE name = 'Bob';" > 12-no_cheating.sql

echo "-- Script to remove all records with a score <= 5 in the table second_table
DELETE FROM second_table WHERE score <= 5;" > 13-change_class.sql

echo "-- Script to compute the score average of all records in the table second_table
SELECT AVG(score) AS average FROM second_table;" > 14-average.sql

echo "-- Script to list the number of records with the same score in the table second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;" > 15-groups.sql

echo "-- Script to list all records of the table second_table without rows without a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;" > 16-no_link.sql

echo "-- Script to convert hbtn_0c_0 database and its table to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;" > 100-move_to_utf8.sql

echo "-- Script to display the average temperature by city ordered by temperature (descending)
SELECT city, AVG(temperature) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;" > 101-avg_temperatures.sql

echo "-- Script to display the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(temperature) as avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;" > 102-top_city.sql

echo "-- Script to display the max temperature of each state (ordered by State name)
SELECT state, MAX(temperature) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;" > 103-max_state.sql
