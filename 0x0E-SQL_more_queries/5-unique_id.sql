-- Script that creates a table
-- Query to create a table unique_id with a unique default value
CREATE TABLE IF NOT EXISTS unique_id (
id INT UNIQUE DEFAULT 1,
name VARCHAR(256));
