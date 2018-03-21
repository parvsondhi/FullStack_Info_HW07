from flask import session
import sqlite3 as sql

def insert_data(trip_name, destination, friend, username):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
    	cur = con.cursor()
    	cur.execute("insert into trips (trip_name, destination, friend, username) VALUES (?, ?, ?, ?)", (trip_name, destination, friend, username))
    	con.commit()

def insert_address(street_address, city, state, country, zip_code):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
    	cur = con.cursor()
    # do something like this later.
    	cur.execute("insert into address (street_address, city, state, country, zip_code) VALUES (?,?,?,?,?)", (street_address, city, state, country, zip_code))
    	con.commit()

def fetch_companions(Trips, username):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("SELECT username FROM Trips GROUP BY username")
        return cur.fetchall()

def retrieve_trips(customer_id, destination, friend):
    username = ''
    if "username" in session:
        username = session["username"]
        print (username) 
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
    	con.row_factory = sql.Row
    	# above sets up connection to accept data in the form of row objects
    	cur = con.cursor()
    	result = cur.execute('SELECT * FROM Trips WHERE Username=?', (username,)).fetchall()
    	print (result)
    return result

def delete_trips(destination, friend):
    username = ''
    if "username" in session:
        username = session["username"]
        print (username) # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        # above sets up connection to accept data in the form of row objects
        cur = con.cursor()
        result = cur.execute('DELETE * FROM Trips WHERE Username=?', (username,)).fetchall()
        print (result)
    return result
	
def retrieve_companions(destination, username):
    username = ''
    if "username" in session:
        username = session["username"]
        print (username)
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
    	con.row_factory = sql.Row
    	# above sets up connection to accept data in the form of row objects
    	cur = con.cursor()
    	result = cur.execute('SELECT * FROM Trips WHERE Friend=?', (username,)).fetchall()
    	print (result)
    return result

