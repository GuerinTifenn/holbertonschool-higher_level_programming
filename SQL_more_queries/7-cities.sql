-- Create the table cities with a FOREIGN KEY that references the states table
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id));
