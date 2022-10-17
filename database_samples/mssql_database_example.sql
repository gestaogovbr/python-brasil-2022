DROP DATABASE IF EXISTS sampledatabase
GO

CREATE DATABASE sampledatabase
GO

USE sampledatabase
GO

create table People (
	id INT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	gender VARCHAR(50),
	country VARCHAR(50),
	company VARCHAR(50),
	personal_address VARCHAR(50),
	date_modified DATETIME2
)

create table Movie (
	id INT,
	movie_title VARCHAR(200),
	movie_genre VARCHAR(200)
)