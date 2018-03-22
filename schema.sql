-- Insert code to create Database Schema
-- This will create your .db database file for use
-- DROP TABLE if exists users;
-- DROP TABLE if exists trips;

-- CREATE TABLE users (
--   user_id INTEGER primary key, username TEXT not null, password TEXT not null
-- );
CREATE TABLE users (
  username TEXT not null, password TEXT not null
);

-- CREATE TABLE trips (
--   trip_id INTEGER PRIMARY KEY, trip_name TEXT not null, destination TEXT not null);

CREATE TABLE trips (
 trip_name TEXT not null, destination TEXT not null);
  -- FOREIGN KEY(user_id) REFERENCES users(user_id));


