-- Script to create the first_table if it does not exist

USE @dbName;

/* Create the first_table if it does not exist */
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);