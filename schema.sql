-- Insert code to create Database Schema
-- This will create your .db database file for use
CREATE TABLE users (
first_name TEXT, last_name TEXT, email TEXT
);

CREATE TABLE trips (
id INTEGER PRIMARY KEY, 
destination TEXT, trip_name TEXT
);

-- CREATE TABLE orders (
-- order_id INTEGER PRIMARY KEY, part_name TEXT, manufacturer TEXT, customer_id INTEGER
-- );

-- CREATE TABLE customer_orders (
-- order_id INTEGER ,customer_id INTEGER
-- );

