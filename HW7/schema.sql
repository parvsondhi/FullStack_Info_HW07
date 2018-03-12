drop table if exists users;
create table users(
  customer_id integer primary key,
  first_name text not null,
  last_name text not null,
  company text not null,
  email text not null,
  phone integer not null
);

drop table if exists trips;
create table trips(
  order_id integer primary key,
  name_of_part text not null,
  manufacturer_of_part text not null,
  customer_id integer not null,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

drop table if exists users_trips;
create table users_trips(
  id integer primary key,
  customer_id integer not null,
  order_id integer not null,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
