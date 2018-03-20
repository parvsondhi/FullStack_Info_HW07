import sqlite3 as sql

DATABASE_FILE = 'ACME.db'

def insert_customer_data(data):
    # SQL statement to insert into database goes here
    conn = sql.connect(DATABASE_FILE)
    c = conn.cursor()

    c.execute("INSERT INTO customers (first_name, last_name, company, email, phone) VALUES (?,?,?,?,?)", data[:5])
    c.execute("INSERT INTO addresses (street, city, state, country, zipcode) VALUES (?,?,?,?,?)", data[5:])

    conn.commit()
    conn.close()

def insert_order_data(data):
    # SQL statement to insert into database goes here
    conn = sql.connect(DATABASE_FILE)
    c = conn.cursor()

    c.execute("INSERT INTO orders (part_name, manufacturer, customer_id) VALUES (?,?,?)", data)

    conn.commit()
    conn.close()

def retrieve_customers():
    # SQL statement to query database goes here
    conn = sql.connect(DATABASE_FILE)
    c = conn.cursor()

    select_cmd = """
    SELECT
        customer_id,
        first_name,
        last_name,
        company,
        email,
        phone
    FROM
        customers
    """
    c.execute(select_cmd)
    result = c.fetchall()

    conn.commit()
    conn.close()

    return result

def retrieve_orders():
    # SQL statement to query database goes here
    conn = sql.connect(DATABASE_FILE)
    c = conn.cursor()

    select_cmd = """
    SELECT
        part_name,
        manufacturer,
        customer_id
    FROM
        orders
    """
    c.execute(select_cmd)
    result = c.fetchall()

    conn.commit()
    conn.close()

    return result

##You might have additional functions to access the database
