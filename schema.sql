drop table if exists users;
drop table if exists trips;
drop table if exists tracker;


CREATE TABLE users (
    user_id integer primary key,
    user_name text,
    password text
);

CREATE TABLE trips (
    trip_id integer primary key,
    trip_name text,
    destination text
);

CREATE TABLE tracker (
    user_id integer,
    trip_id integer,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(trip_id) REFERENCES trips(trip_id)
);
