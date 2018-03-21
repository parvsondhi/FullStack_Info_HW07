drop table if exists users;
create table users(
  user_id integer primary key,
  first_name text not null,
  last_name text not null,
  username text not null,
  password text not null
);

drop table if exists trips;
create table trips(
  trip_id integer primary key,
  owner text not null,
  destination text not null,
  trip_name text not null,
  friend text not null
);