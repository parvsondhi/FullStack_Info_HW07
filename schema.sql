-- -- Insert code to create Database Schema
-- -- This will create your .db database file for use

drop table if exists users;
create table users(
	user_id integer primary key,
	username text not null,
	password text not null
);

drop table if exists trips;
create table trips(
	trip_id integer primary key,
	user_id integer not null,
	trip text not null,
	destination text not null,
	friend text not null,
	friend_id integer not null,
	FOREIGN KEY(user_id) REFERENCES users(user_id)
);