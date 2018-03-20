from __future__ import print_function
import sqlite3 as sql

import sys


def insert_user(user_name,password):
    with sql.connect("app.db") as con:
        message = "SQL insert user failed"
        cur = con.cursor()
        cur.execute("INSERT INTO users (user_name, password) VALUES (?,?)", (user_name, password))
        con.commit()
        message = "SQL insert user succeeded"
    return message

def insert_trips(trip_name,destination,users):
    with sql.connect("app.db") as con:
        message = "SQL insert trips failed"
        cur = con.cursor()
        cur.execute("INSERT INTO trips (trip_name, destination) VALUES (?,?)", (trip_name, destination))
        trip_id = cur.lastrowid  # Get id of the new trip.
        for user in users:
            user_id = get_userid_from_name(user)
            print("Trip id is {}, user name is {} u_id is {}".format(trip_id, user, user_id), file=sys.stderr)
            if user_id < 0:
                continue
            cur.execute("INSERT INTO tracker (trip_id, user_id) VALUES (?,?)", (trip_id, user_id))
        con.commit()
        message = "SQL insert trips succeeded"
    return message

def retrieve_users():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select user_name, user_id from users").fetchall()
    return result

def get_userid_from_name(user_name):
    if user_name is None:
        return -1
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select user_id from users where user_name ='" + user_name + "'").fetchone()
    if result is None:
        return -1  # No such user.
    return result['user_id']

def recognize_user(user_name, password):
    if user_name is None:
        return False
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select password from users where user_name ='" + user_name +
            "' and password ='" + password +"'").fetchone()
    return (result is not None)


def retrieve_trips(user_name):
    user_id = get_userid_from_name(user_name)
    if user_id < 0:
        return None
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        # Select trips linked to the given user.
        result = cur.execute("select trips.trip_id as trip_id, trips.trip_name as trip_name, trips.destination as destination \
            from trips inner join tracker on trips.trip_id=tracker.trip_id and user_id=" + str(user_id)).fetchall()
    return result

def remove_trip(trip_id):
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("delete from trips where trip_id = " + trip_id)
    return result

