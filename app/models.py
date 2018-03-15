import sqlite3 as sql
from app import login, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sys

class User(UserMixin):

	def __init__(self, username):
		self.id = 0;
		self.username = username
		self.email = ""
		self.password_hash = ""

	def __repr__(self):
		return '<User {}>'.format(self.username)

	# @property
	# def get_id(self):
	# 	return self.username

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	@staticmethod
	def get(userid):
		with sql.connect('database.db') as connection:
			connection.row_factory = sql.Row
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM users WHERE username=?", (userid,))
			result = cursor.fetchall()
			if len(result) == 0:
				return None
			else:
				user = User(userid)
				row = result[0]
				user.id = row[0]
				user.email = row[2]
				user.password_hash = row[3]
				return user

def set_password(password):
		return generate_password_hash(password)


@login.user_loader
def load_user(id):
	return User.get(id)

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

def check_username_exists(query):
	with sql.connect('database.db') as connection:
		connection.row_factory = sql.Row
		cursor = connection.cursor()
		cursor.execute("SELECT username FROM users WHERE username=?", (query,))
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
