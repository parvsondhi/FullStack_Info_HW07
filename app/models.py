import sqlite3 as sql

def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect("app.db") as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        result = cur.execute("select * from customers").fetchall()
    return result

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect("app.db") as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        result = cur.execute("select o.name_of_part, o.manufacturer_of_part, co.customer_id from orders as o, customers_orders as co where o.order_id = co.order_id").fetchall()
    return result


##You might have additional functions to access the database
def insert_customer(first_name, last_name, company, email, phone):
    with sql.connect("app.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO customers(first_name, last_name, company, email, phone) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, company, email, phone))
        customer_id = cur.execute('SELECT last_insert_rowid()').fetchone()[0]
        conn.commit()
    return customer_id

def insert_address(address, city, state, country, zip_code, customer_id):
    with sql.connect("app.db") as conn:
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO addresses(street_address, city, state, country, zip_code, customer_id) VALUES (?, ?, ?, ?, ?, ?)", (address, city, state, country, zip_code, customer_id))
        conn.commit()

def insert_order(name, manufacturer, customer_id):
    with sql.connect("app.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO orders(name_of_part, manufacturer_of_part) VALUES (?, ?)", (name, manufacturer))
        order_id = cur.execute('SELECT last_insert_rowid()').fetchone()[0]
        cur.execute("INSERT INTO customers_orders(customer_id, order_id) VALUES (?, ?)", (customer_id, order_id))
        conn.commit()
