import sqlite3 as sql


def insert_customer(first_name, last_name, company, email, phone_number):
    # SQL statement to insert into database goes here
    with sql.connect('database.db') as con:
    	cur = con.cursor() # creating cursor
    	cur.execute("INSERT INTO customers (first_name, last_name, company, email, phone_number) VALUES (?,?,?,?,?)",
    		(first_name, last_name, company, email, phone_number))
    	con.commit() # commit is like save

def insert_address(street_address, city, state, country, zipcode, customer_id):
	with sql.connect('database.db') as con:
		cur = con.cursor()
		cur.execute("INSERT INTO address (street_address, city, state, country, zipcode, customer_id) VALUES (?,?,?,?,?,?)", 
			(street_address, city, state, country, zipcode, customer_id))
		con.commit()

def insert_orders(name_of_part, manufacturer_of_part, customer_id):
	with sql.connect('database.db') as con:
		cur = con.cursor()
		cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part, customer_id) VALUES (?,?,?)", (name_of_part, manufacturer_of_part, customer_id))
		con.commit()

def insert_order_detail(customer_id, order_id):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO order_detail (customer_id, order_id) VALUES (?,?)", (customer_id, order_id))
        con.commit()

def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect('database.db') as con:
    	con.row_factory = sql.Row # setting up connection to collect data in row object
    	cur = con.cursor()
    	result = cur.execute("SELECT * FROM customers").fetchall()
    	return result

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect('database.db') as con:
    	con.row_factory = sql.Row
    	cur = con.cursor()
    	result = cur.execute("SELECT * FROM orders").fetchall()
    	return result


##You might have additional functions to access the database
def retrieve_customer_id():
    with sql.connect('database.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM customers ORDER BY customer_id DESC LIMIT 1").fetchall()
        for row in result:
            return row[0]

def retrieve_order_id():
    with sql.connect('database.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM orders ORDER BY order_id DESC LIMIT 1").fetchall()
        for row in result:
            return row[0]

