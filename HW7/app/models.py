import sqlite3 as sql
from flask import session, escape
import sys

#TODO: remove print
def retrieve_trips(curr_user):
    query = "SELECT * FROM trips WHERE owner == '" + curr_user + "' OR friend == '" + curr_user+"'"
    print(query, file=sys.stderr)
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute(query).fetchall()
        con.commit()
    return result

def insert_trip(trip_owner, dest, trip_name, friend):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO trips (owner, destination, trip_name, friend) VALUES (?,?,?,?)", (trip_owner, dest, trip_name, friend))
        con.commit()


def delete_trip(value):
     with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM trips WHERE trip_id == " + value)
        con.commit()

#TODO: replace the test curr_user with real curr_user
def retrieve_friends(curr_user):
    #curr_user = session['username']
    #curr_user = "'cy'"
    query = "SELECT username FROM users WHERE username != '" + curr_user + "'"
    print(query, file=sys.stderr)
    with sql.connect("database.db") as con:        
        #con.row_factory = sql.Row
        con.row_factory = lambda cursor, row: row[0]
        cur = con.cursor()
        result = cur.execute(query).fetchall()
        con.commit()
    return result

def insert_user(username, password, first_name, last_name):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users (username, password, first_name, last_name) VALUES (?,?,?,?)", (username, password, first_name, last_name))
        con.commit()
    return cur.lastrowid

def google_maps():
    return None
