import sqlite3 as sql
from flask import session, escape

# I think retrieve trips will be better
def retrieve_trips():
    return none

# change name to insert_trip
def insert_trip(dest, friend, trip_name, trip_owner):

    return none

# remove trip column from the table trips
def delete_trip():
    # DELETE FROM table_name WHERE some_column=some_value;
    # ex: Delete from users where name = ‘eric’
    return none

# change name to retrieve_user
# retrieve all user for the dropdown in the "creat"
#def retrieve_friends():
def retrieve_friends():
    #curr_user = escape(session['username'])
    curr_user = "'cy'"
    query = "SELECT username FROM users WHERE username != " + curr_user
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute(query).fetchall()
    return result

# change name to insert_user
# def create_user():
def insert_user(username, password, first_name, last_name):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO user (username, password, first_name, last_name) VALUES (?,?,?,?)", (username, password, first_name, last_name))
        con.commit()
    return cur.lastrowid

def retrieve_userID():
    curr_user = escape(session['username'])
    query = "SELECT user_id FROM users WHERE username ==" + curr_user
    with sql.connect("database.db") as con:
        cur = con.cursor()
        result = cur.execute(query)
    return result


def google_maps():
    return none
