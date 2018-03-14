import sqlite3 as sql
from app import login, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sys

class User(UserMixin):

	def __init__(self, username):
		self.id = username
		self.password_hash = 'abc';

	def __repr__(self):
		return '<User {}>'.format(self.username)

	# def get_id(u):
	# 	with sql.connect('database.db') as connection:
 #    	cursor = connection.cursor()
 #    	cursor.execute("SELECT user_id where username = ")
 #    	connection.commit()


	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

def set_password(password):
		return generate_password_hash(password)

@login.user_loader
def load_user(id):
    return User.get(user_id)


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


def create_user(username, email, password):
    with sql.connect('database.db') as connection:
    	cursor = connection.cursor()
    	cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (?,?, ?)",(username, email, set_password(password)))
    	connection.commit()

def check_username_exists(query):
	with sql.connect('database.db') as connection:
		connection.row_factory = sql.Row
		cursor = connection.cursor()
		cursor.execute("SELECT username from users where username=?", (query,))
		result = cursor.fetchall()
		# print(result, file=sys.stderr)
		if len(result) == 0:
			# print("nothing found", file=sys.stderr)
			return False
		else:
			# print("something found", file=sys.stderr)
			return True


# def retrieve_customer_id():
# 	with sql.connect('database.db') as connection:
# 		connection.row_factory = sql.Row
# 		cursor = connection.cursor()
# 		result = cursor.execute("SELECT * FROM customers ORDER BY customer_id DESC LIMIT 1").fetchall()
# 		for row in result:
# 			return row[0]
