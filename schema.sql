-- Insert code to create Database Schema
-- This will create your .db database file for use
drop table if exists customers;
create table customers (
	customer_id integer primary key,
	first_name text not null,
	last_name text not null,
	company text not null,
	email text not null,
	phone text not null
);

drop table if exists addresses;
create table addresses (
	id integer primary key,
	street_address text not null,
	city text not null,
	state text not null,
	country text not null,
	zip_code text not null

);

drop table if exists orders;
create table orders (
	order_id integer primary key,
	name_of_part text not null,
	manufacturer_of_part text not null,
	customer_id integer not null,
	Foreign key(customer_id) references customers(customer_id)
);

drop table if exists customer_orders;
create table customer_orders (
	id integer primary key,
	order_id integer not null,
	customer_id integer not null,
	Foreign key(order_id) references orders(order_id),
	Foreign key(customer_id) references customers(customer_id)
);