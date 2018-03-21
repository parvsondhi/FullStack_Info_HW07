import sqlite3 as sql
from flask import session, escape
import sys

# I think retrieve trips will be better
def retrieve_trips():
    #curr_user = escape(session['username'])
    curr_user = "'cy'"
    query = "SELECT * FROM trips WHERE owner == " + curr_user + "OR friend == " + curr_user
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute(query).fetchall()
    return result

def insert_trip(trip_owner, dest, trip_name, friend):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO trips (owner, destination, trip_name, friend) VALUES (?,?,?,?)", (trip_owner, dest, trip_name, friend))
        con.commit()

# remove trip column from the table trips
def delete_trip(value):
     with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM trips WHERE trip_id == " + value)
        con.commit()

def retrieve_friends():
    #curr_user = escape(session['username'])
    #curr_user = "'cy'"
    #query = "SELECT username FROM users WHERE username != " + curr_user
    query = "SELECT * FROM users"
    print(query, file=sys.stderr)
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute(query).fetchall()
        for row in con.execute(query):
            print(row, file=sys.stderr) 
        con.commit()
    return result

def insert_user(username, password, first_name, last_name):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO user (username, password, first_name, last_name) VALUES (?,?,?,?)", (username, password, first_name, last_name))
        con.commit()
    return cur.lastrowid

def google_maps():
    return none
