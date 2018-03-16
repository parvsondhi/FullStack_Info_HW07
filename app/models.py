import sqlite3 as sql

def insert_data(customer_data, address_data):
	# SQL statement to insert into database goes here
	with sql.connect('database.db') as con:
		cur = con.cursor()
		cur.execute("INSERT INTO customers (first_name, last_name, company, email, phone) VALUES (?,?,?,?,?)", customer_data)
		cur.execute("INSERT INTO addresses (street_address, city, state, country, zip_code) VALUES (?,?,?,?,?)", address_data)
		con.commit()

def retrieve_customers():
	# SQL statement to query database goes here
	with sql.connect('database.db') as con:
		con.row_factory = sql.Row 
		cur = con.cursor()
		customers = cur.execute("SELECT * FROM customers").fetchall()
		return customers

def retrieve_orders():
	# SQL statement to query database goes here
	with sql.connect('database.db') as con:
		con.row_factory = sql.Row 
		cur = con.cursor()
		orders = cur.execute("SELECT * FROM orders").fetchall()
		return orders

def insert_order(order_data):
	with sql.connect('database.db') as con:
		cur = con.cursor()
		cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part, customer_id) VALUES (?,?,?)", order_data)
		con.commit()
		return cur.lastrowid #return id to pass to customer orders

def insert_customer_order(order_id, customer_id):
	with sql.connect('database.db') as con:
		cur = con.cursor()
		cur.execute("INSERT INTO customer_orders (order_id, customer_id) VALUES (?,?)", (order_id, customer_id))
		con.commit()

##You might have additional functions to access the database
def get_customer_id():
	with sql.connect('database.db') as connection:
		connection.row_factory = sql.Row
		cursor = connection.cursor()
		result = cursor.execute("SELECT * FROM customers ORDER BY customer_id DESC LIMIT 1").fetchall()
		for row in result:
			return row[0]

def get_order_id():
	with sql.connect('database.db') as connection:
		connection.row_factory = sql.Row
		cursor = connection.cursor()
		result = cursor.execute("SELECT * FROM orders ORDER BY order_id DESC LIMIT 1").fetchall()
		for row in result:
			return row[0]