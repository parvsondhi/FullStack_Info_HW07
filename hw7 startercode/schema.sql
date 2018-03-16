CREATE TABLE customer (
    customer_id integer primary key,
    first_name text,
    last_name text,
    company text,
    email text,
    phone text
);

CREATE TABLE address (
    id integer primary key,
    street_address text,
    city text,
    state text,
    country text,
    zip_code text,
    customer_id integer
);

CREATE TABLE purchase_order (
    order_id integer primary key,
    name_of_part text,
    manufacturer_of_part text
);

CREATE TABLE customer_order (
    id integer primary key,
    order_id integer,
    customer_id integer
);

