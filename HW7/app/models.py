import sqlite3 as sql

def login():

def logout():

def signup():

def retrieve_trips():

def create_trip():

def delete_trip():

def retrieve_friends():

def create_user():

def google_maps():

###############################################################################################################################################

def insert_customer(first_name, last_name, company, email, phone):
    # SQL statement to insert into database goes here
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO customers (first_name, last_name, company, email, phone) VALUES (?,?,?,?,?)", (first_name, last_name, company, email, phone))
        con.commit()
    return cur.lastrowid

def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select * from customers").fetchall()
    return result

def insert_order(name_of_part, manufacturer_of_part, customer_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part, customer_id) VALUES (?,?,?)", (name_of_part, manufacturer_of_part, customer_id))
        con.commit()
    return cur.lastrowid

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select * from orders").fetchall()
    return result

def insert_address(street_address, city, state, country, zip_code, customer_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO address (street_address, city, state, country, zip_code, customer_id) VALUES (?,?,?,?,?,?)", (street_address, city, state, country, zip_code, customer_id))
        con.commit()
    return cur.lastrowid

def insert_customer_order(customer_id, order_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO customers_orders (customer_id, order_id) VALUES (?,?)", (customer_id, order_id))
        con.commit()
    return cur.lastrowid
