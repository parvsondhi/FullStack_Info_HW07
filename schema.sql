-- Insert code to create Database Schema
-- This will create your .db database file for use
drop table if exists users;
create table users (
	username text primary key,
	password text not null
);

drop table if exists trips;
create table trips (
	id integer primary key,
    name text not null,
    destination text not null,
    user1 text not null,
    user2 text,    
    FOREIGN KEY(user1) REFERENCES users(username)
);
