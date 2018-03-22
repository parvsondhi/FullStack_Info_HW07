-- Insert code to create Database Schema
-- This will create your .db database file for use
-- drop table if exists users;
-- drop table if exists addresses;
-- drop table if exists trips;

create table users(
	email_id text primary key,
	password text not null, 
	first_name text not null,
	last_name text not null
);

create table trips(
	trip_id integer primary key,
	name text not null,
	location text not null,
	email_id1 text not null,
	email_id2 text not null
); 
