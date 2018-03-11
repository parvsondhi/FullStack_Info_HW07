import sqlite3 as sql

def insert_trip(destination, friend):
    with sql.connect('database.db') as connection:
    	cursor = connection.cursor()
    	cursor.execute("INSERT INTO trips (destination, friend) VALUES (?,?)",(destination, friend))
    	connection.commit()


def retrieve_trips():
    with sql.connect('database.db') as connection:
    	connection.row_factory = sql.Row
    	cursor = connection.cursor()
    	result = cursor.execute("SELECT * FROM trips").fetchall()
    	return result



# def retrieve_customer_id():
# 	with sql.connect('database.db') as connection:
# 		connection.row_factory = sql.Row
# 		cursor = connection.cursor()
# 		result = cursor.execute("SELECT * FROM customers ORDER BY customer_id DESC LIMIT 1").fetchall()
# 		for row in result:
# 			return row[0]
