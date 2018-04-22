drop table if exists trips;
create table trips (
	customer_id integer primary key,
	trip_name text not null,
	destination text not null,
	friend text not null,
	username text not null
);





