-- Insert code to create Database Schema
-- This will create your .db database file for use
DROP TABLE if exists customers;
DROP TABLE if exists addresses;
DROP TABLE if exists orders;
DROP TABLE if exists customers_orders;

CREATE TABLE customers (
       customer_id INTEGER PRIMARY KEY,
       first_name TEXT not null,
       last_name TEXT not null,
       company TEXT not null,
       email TEXT not null,
       phone INTEGER not null
);

CREATE TABLE addresses (
	id INTEGER PRIMARY KEY,
	street_address TEXT not null,
	city TEXT not null,
	state TEXT not null,
	country TEXT not null,
	zip_code INTEGER not null,
	customer_id INTEGER not null,
	FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE orders (
	order_id INTEGER PRIMARY KEY,
	name_of_part TEXT not null,
	manufacturer_of_part TEXT not null
);

CREATE TABLE customers_orders (
	id INTEGER PRIMARY KEY,
	customer_id INTEGER not null,
	order_id INTEGER not null,
	FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
	FOREIGN KEY(order_id) REFERENCES orders(order_id)
);