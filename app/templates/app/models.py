import sqlite3 as sql

def insert_data():
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
            cur = con.cursor()

def retrieve_customers():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select * from customers").fetchall()
        print (result)
    return result

def retrieve_orders():
    ## TODO: join with customer_orders table
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        query = "select c.company, o.part_name, o.manufacturer FROM customers AS c, customers_orders AS co LEFT JOIN orders As o ON co.order_id = o.order_id WHERE c.customer_id = co.customer_id"
        result = cur.execute(query).fetchall()
        print (result)
    return result

def retrieve_addressess():
    with sql.connect("app.db") as con:
        cur = con.cursor()
        result = cur.execute("select * from addressess").fetchall()
        print (result)
    return result

def insert_customer(company, email, fname, lname, phone):
    ## SQL statement to insert into Database
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO customers (company, email, fname, lname, phone) VALUES (?,?,?,?,?)",(company, email, fname, lname, phone))
        con.commit()
        customer_id = cur.lastrowid
        return customer_id

def insert_address(customer_id, street_address, city, state, country, zip_code):
    ## SQL statement to insert into Database
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO addressess (customer_id, street_address, city, state, country, zip_code) VALUES (?,?,?,?,?,?)",(customer_id, street_address, city, state, country, zip_code))
        con.commit()


def insert_order(customer_id, part_name, manufacturer):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        ## insert order into table
        cur.execute("INSERT INTO orders (part_name, manufacturer) VALUES (?,?)", (part_name, manufacturer))
        con.commit()

        ## get last ID
        order_id = cur.lastrowid

        ## insert into customers_orders
        cur.execute("INSERT INTO customers_orders (customer_id, order_id) VALUES (?,?)", (customer_id, order_id))
        con.commit()
