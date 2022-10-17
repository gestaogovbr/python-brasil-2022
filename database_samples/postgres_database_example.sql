CREATE DATABASE sampledatabase;
\c sampledatabase

DROP TABLE IF EXISTS People;

Create table People (
	id INT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	gender VARCHAR(50),
	country VARCHAR(50),
	company VARCHAR(50),
	personal_address VARCHAR(50),
	date_modified TIMESTAMP
)