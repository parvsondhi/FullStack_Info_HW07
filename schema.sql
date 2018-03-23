DROP TABLE if exists users;
DROP TABLE if exists trips;

CREATE TABLE users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT not null,
  password TEXT not null
);

CREATE TABLE trips (
  trip_id INTEGER PRIMARY KEY AUTOINCREMENT,
  trip_name TEXT not null,
  destination TEXT not null,
  travel_pal TEXT not null,
  trip_creator TEXT not null
  -- FOREIGN KEY(user_id) REFERENCES users(user_id)
  );
