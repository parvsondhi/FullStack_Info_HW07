-- Insert code to create Database Schema
-- This will create your .db database file for use
DROP TABLE users;
DROP TABLE trips;

CREATE TABLE users(
    email TEXT,
    password TEXT,
    salty TEXT
);

CREATE TABLE trips(
    trip_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    dest TEXT,
    email1 TEXT,
    email2 TEXT
);
