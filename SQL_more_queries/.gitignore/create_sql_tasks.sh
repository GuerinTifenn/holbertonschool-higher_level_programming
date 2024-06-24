#!/bin/bash

# Create users and grant privileges
echo "-- Create user user_0d_1 and grant all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Create user user_0d_2 and grant select privilege on hbtn_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';" > create_users_and_privileges.sql

# Task 0: My privileges!
echo "-- List all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost)
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';" > 0-privileges.sql

# Task 1: Root user
echo "-- Create the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" > 1-create_user.sql

# Task 2: Read user
echo "-- Create the database hbtn_0d_2 and the user user_0d_2 with SELECT privilege
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';" > 2-create_read_user.sql

# Task 3: Always a name
echo "-- Create the table force_name with a NOT NULL constraint on the name column
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);" > 3-force_name.sql

# Task 4: ID can't be null
echo "-- Create the table id_not_null with a default value of 1 for the id column
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));" > 4-never_empty.sql

# Task 5: Unique ID
echo "-- Create the table unique_id with a unique constraint on the id column
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));" > 5-unique_id.sql

# Task 6: States table
echo "-- Create the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);" > 6-states.sql

# Task 7: Cities table
echo "-- Create the table cities with a FOREIGN KEY that references the states table
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id));" > 7-cities.sql

# Task 8: Cities of California
echo "-- List all the cities of California in the database hbtn_0d_usa
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;" > 8-cities_of_california_subquery.sql

# Task 9: Cities by States
echo "-- List all cities contained in the database hbtn_0d_usa with their states
SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id ORDER BY cities.id ASC;" > 9-cities_by_state_join.sql

# Task 10: Genre ID by show
echo "-- List all shows in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres WHERE tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;" > 10-genre_id_by_show.sql

# Task 11: Genre ID for all shows
echo "-- List all shows in the database hbtn_0d_tvshows with their genre IDs
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;" > 11-genre_id_all_shows.sql

# Task 12: No genre
echo "-- List all shows in hbtn_0d_tvshows without a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id WHERE tv_show_genres.genre_id IS NULL ORDER BY tv_shows.title ASC;" > 12-no_genre.sql

# Task 13: Number of shows by genre
echo "-- List all genres from hbtn_0d_tvshows and the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id GROUP BY tv_genres.name HAVING number_of_shows > 0 ORDER BY number_of_shows DESC;" > 13-count_shows_by_genre.sql

# Task 14: My genres
echo "-- List all genres of the show Dexter
SELECT tv_genres.name FROM tv_genres, tv_show_genres, tv_shows WHERE tv_shows.id = tv_show_genres.show_id AND tv_show_genres.genre_id = tv_genres.id AND tv_shows.title = 'Dexter' ORDER BY tv_genres.name ASC;" > 14-my_genres.sql

# Task 15: Only Comedy
echo "-- List all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title FROM tv_shows, tv_show_genres, tv_genres WHERE tv_shows.id = tv_show_genres.show_id AND tv_show_genres.genre_id = tv_genres.id AND tv_genres.name = 'Comedy' ORDER BY tv_shows.title ASC;" > 15-comedy_only.sql

# Task 16: List shows and genres
echo "-- List all shows and their genres from the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_genres.name FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id ORDER BY tv_shows.title ASC, tv_genres.name ASC;" > 16-shows_by_genre.sql

# Task 17: Go to UTF8
echo "-- Convert hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CHANGE name name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;" > 100-move_to_utf8.sql

# Task 18: Temperatures #0
echo "-- Display the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;" > 101-avg_temperatures.sql

# Task 19: Temperatures #1
echo "-- Display the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp FROM temperatures WHERE month IN ('July', 'August') GROUP BY city ORDER BY avg_temp DESC LIMIT 3;" > 102-top_city.sql

# Task 20: Temperatures #2
echo "-- Display the max temperature of each state ordered by State name
SELECT state, MAX(temperature) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC;" > 103-max_state.sql

# Make the script executable
chmod +x create_sql_tasks.sh
