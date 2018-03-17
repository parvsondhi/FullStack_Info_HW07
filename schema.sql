-- Insert code to create Database Schema
-- This will create your .db database file for use
drop table if exists trips;
create table trips (
    trip_id integer primary key,
    tripname text not null,
    destination text not null
);
drop table if exists users;
create table users (
    user_id integer primary key,
    username text not null,
    email text not null,
    password_hash text not null
);

drop table if exists users_on_trips;
create table users_on_trips (
	user_trip_id integer primary key,
	user_id integer not null, 
	trip_id integer not null, 
	FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE, 
	FOREIGN Key(trip_id) REFERENCES trips(trip_id) ON DELETE CASCADE

);
-- drop table if exists customer_order;
-- create table customer_order(
--  id integer primary key,
--  customer_id integer not null,
--  order_id integer not null,
--  FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
--  FOREIGN KEY(order_id) REFERENCES orders(order_id)
-- );