import sqlite3 as sql

DATABASE_FILE = 'ACME.db'

def insert_customer_data(company, email, first_name, last_name, phone, street_address, city, state, country, zip_code):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as database:
        cursor = database.cursor()
    
        cursor.execute('INSERT INTO customers (first_name, last_name, company, email, phone) VALUES (?,?,?,?,?)', (first_name, last_name, company, email, phone))
        cursor.execute("INSERT INTO addresses (street_address, city, state, country, zip_code) VALUES (?,?,?,?,?)", (street_address, city, state, country, zip_code))

    database.commit()
    database.close()

def insert_order_data(value, part_name,manufacturer):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO orders (part_name, manufacturer) VALUES (?,?)", (part_name, manufacturer))
        cur.execute("INSERT INTO customer_orders (customer_id, order_id ) VALUES (?,?)", (value, value))
        con.commit()
def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect("app.db") as database:
        database.row_factory = sql.Row
        cur = database.cursor()
        result = cur.execute("SELECT * FROM customers").fetchall()

    return result

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect("app.db") as database:
        database.row_factory = sql.Row
        cur = database.cursor()
        result = cur.execute("SELECT * FROM orders").fetchall()

    return result
