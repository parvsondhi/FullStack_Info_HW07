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
  name text not null,
  friend text not null,
  user_id integer not null,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

drop table if exists users_trips;
create table users_trips(
  id integer primary key,
  user_id integer not null,
  trip_id integer not null,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (trip_id) REFERENCES trips(trip_id)
);
