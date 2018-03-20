import sqlite3 as sql

def insert_trip(user_id,trip,destination,friend,friend_id):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("INSERT INTO trips (user_id, trip, destination, friend, friend_id) VALUES (?,?,?,?,?)",(user_id,trip,destination,friend, friend_id))
		con.commit()
	return cur.lastrowid

def retrieve_trips(username):
	with sql.connect("database.db") as con:
		con.row_factory = sql.Row
		cur = con.cursor()
		result = cur.execute("select * from trips, users WHERE trips.user_id = users.user_id AND users.username=(?)", [username]).fetchall()
		return result

def retrieve_user(username):
	with sql.connect("database.db") as con:
		con.row_factory = sql.Row
		cur = con.cursor()
		result = cur.execute("select * from users WHERE username=(?)",[username]).fetchall()
		return result[0][0]

def insert_user(): # keep this function for signup
	pass

def check_user(username,password):
	with sql.connect("database.db") as con:
		con.row_factory = sql.Row
		cur = con.cursor()
		result = cur.execute("select * from users WHERE username=(?) AND password = (?)", [username,password]).fetchall()
		if len(result) == 0:
			return False
		else:
			user = result[0]
			return user

def retrieve_allusers():
    with sql.connect("database.db") as con:
    	con.row_factory = sql.Row
    	cur = con.cursor()
    	result = cur.execute("select * from users").fetchall()
    	return result

def delete_trip(trip):
	with sql.connect("database.db") as con:
		con.row_factory = sql.Row
		cur = con.cursor()
		result = cur.execute("delete from trips where trip=(?)", [trip]).fetchall()