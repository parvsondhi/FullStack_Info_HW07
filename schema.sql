drop table if exists users;
drop table if exists trips;
drop table if exists user_to_trip;

create table users(
	userid integer primary key,
	username text not null,
	password text not null
);

create table trips(
	id integer primary key,
	tripname text not null,
	destination text not null,
	userid_1 integer not null,
	userid_2 integer not null,
	FOREIGN KEY(userid_1) REFERENCES users(userid),
	FOREIGN KEY(userid_2) REFERENCES users(userid)
);

create table user_to_trip(
	id integer primary key,
	userid integer not null,
	tripid integer not null,
	FOREIGN KEY(userid) REFERENCES users(userid),
	FOREIGN KEY(tripid) REFERENCES trips(id)
);