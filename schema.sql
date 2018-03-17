-- Insert code to create Database Schema
-- This will create your .db database file for use
CREATE TABLE users (
user_id INTEGER PRIMARY KEY, 
first_name TEXT, last_name TEXT, email TEXT
);

CREATE TABLE trips (
trip_id INTEGER PRIMARY KEY, 
trip_title TEXT, destination TEXT
);

