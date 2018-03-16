CREATE TABLE customer (
	customer_id int primary key,
	first_name varchar(255),
	last_name varchar(255),
	company varchar(255), 
	email varchar(255), 
	phone varchar(255) 
);

CREATE TABLE address (
	id int primary key,
	street_address varchar(255),
	city varchar(255),
	state varchar(255),
	country varchar(255),
	zip_code varchar(255),
	customer_id int
);

CREATE TABLE order (
	order_id int primary key, 
	name_of_part varchar(255), 
	manufacturer_of_part varchar(255)

);

CREATE TABLE customerOrder (
	id int primary key,
	order_id int foreign key,
	customer_id int foreign key,
);