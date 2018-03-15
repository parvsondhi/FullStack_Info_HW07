import sqlite3 as sql
from app import login_manager, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sys

class User(UserMixin):

	def __init__(self, id, username, email, password_hash):
		self.id = id;
		self.username = username
		self.email = email
		self.password_hash = password_hash


""" Takes a username as parameter and checks in the database. If the user exists, 
returns user object. If not, returns None.
"""
def getUserByUsername(query):
	with sql.connect('database.db') as connection:
		connection.row_factory = sql.Row
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM users WHERE username=?", (userid,))
		result = cursor.fetchall()
		if len(result) == 0:
			return None
		else:
			row = result[0]
			user = User(row[0], username, row[2], row[3])
			return user


""" Takes a userID as parameter and checks in the database. If the user exists, 
returns user object. If not, returns None.
"""
def getUserByID(query):
	with sql.connect('database.db') as connection:
		connection.row_factory = sql.Row
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM users WHERE user_id=?", (query,))
		result = cursor.fetchall()
		if len(result) == 0:
			return None
		else:
			row = result[0]
			user = User(query, row[1], row[2], row[3])
			return user


""" Takes a username as parameter and 
checks with user ID is associated with that username.
Returns the userID. Assumes the username exists.
"""
def getUserID(query):
	with sql.connect('database.db') as connection:
		connection.row_factory = sql.Row
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM users WHERE username=?", (query,))
		result = cursor.fetchall()
		return result[0][0]


# def set_password(password):
# 		return generate_password_hash(password)

@login_manager.user_loader
def load_user(id):
     return getUserByID(id)

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


def create_user(username, email, password_hash):
	with sql.connect('database.db') as connection:
		cursor = connection.cursor()
		cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (?,?, ?)",(username, email, password_hash))
		connection.commit()

# def check_username_exists(query):
# 	with sql.connect('database.db') as connection:
# 		connection.row_factory = sql.Row
# 		cursor = connection.cursor()
# 		cursor.execute("SELECT * FROM users WHERE username=?", (query,))
# 		result = cursor.fetchall()
# 		if len(result) == 0:
# 			# print("nothing found", file=sys.stderr)
# 			return -1
# 		else:
# 			# print("something found", file=sys.stderr)
# 			row = result[0]
# 			return row[3] #returns password hash if exists
	
# def retrieve_customer_id():
# 	with sql.connect('database.db') as connection:
# 		connection.row_factory = sql.Row
# 		cursor = connection.cursor()
# 		result = cursor.execute("SELECT * FROM customers ORDER BY customer_id DESC LIMIT 1").fetchall()
# 		for row in result:
# 			return row[0]
