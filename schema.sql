-- Insert code to create Database Schema
-- This will create your .db database file for use

drop table if exists trips;
create table trips (
	trip_id integer primary key,
	destination text not null,
	friend text not null
);

-- drop table if exists customer_order;
-- create table customer_order(
-- 	id integer primary key,
-- 	customer_id integer not null,
-- 	order_id integer not null,
-- 	FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
-- 	FOREIGN KEY(order_id) REFERENCES orders(order_id)
-- );