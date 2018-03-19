-- Insert code to create Database Schema
-- This will create your .db database file for use

DROP TABLE IF EXISTS users;
CREATE TABLE users(
  user_id INTEGER PRIMARY KEY,
  username TEXT NOT NULL,
  password TEXT NOT NULL);

DROP TABLE IF EXISTS trips;
CREATE TABLE trips(
  trip_id INTEGER PRIMARY KEY,
  trip_name TEXT NOT NULL,
  destination TEXT NOT NULL,
  friend_id INTEGER,
  FOREIGN KEY(friend_id) REFERENCES users(user_id));

DROP TABLE IF EXISTS users_trips;
CREATE TABLE users_trips(
  user_id INTEGER NOT NULL,
  trip_id INTEGER NOT NULL,
  FOREIGN KEY(user_id) REFERENCES users(user_id),
  FOREIGN KEY(trip_id) REFERENCES trips(trip_id));

-- Dummy Data for testing

INSERT into users (username, password)
VALUES ('peter','password');

INSERT into users (username, password)
VALUES ('michelle','password');

INSERT into trips (trip_name, destination, friend_id)
VALUES ('island paradise','alameda', 2);
