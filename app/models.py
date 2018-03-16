import sqlite3 as sql
from flask_login import LoginManager, UserMixin
import hashlib

# def retrieve_customers():
#     with sql.connect("app.db") as con:
#         con.row_factory = sql.Row
#         cur = con.cursor()
#         result = cur.execute("select * from customers").fetchall()
#         print (result)
#     return result

# def validate_user(username, password):
#     with sql.connect("static/app.db") as con:
#         cur = con.cursor()
#         result = cur.execute("SELECT * FROM users").fetchall()
#         for row in result:
#             dbUser = row[0]
#             dbPass = row[1]
#             if dbUser==username:
#     return None

# def get_trips():
#
# def insert_trip():
#
# def delete_trip():
#
# def add_friend():
#
# def login():
