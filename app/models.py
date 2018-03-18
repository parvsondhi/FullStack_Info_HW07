import sqlite3 as sql


def insert_user(user_name,password):
    with sql.connect("app.db") as con:
        message = "SQL insert user failed"
        cur = con.cursor()
        cur.execute("INSERT INTO users (user_name, password) VALUES (?,?)", (user_name, password))
        con.commit()
        message = "SQL insert user succeeded"
    return message

def insert_trips(trip_name,destination):
    with sql.connect("app.db") as con:
        message = "SQL insert trips failed"
        cur = con.cursor()
        cur.execute("INSERT INTO trips (trip_name, destination) VALUES (?,?)", (trip_name, destination))
        con.commit()
        message = "SQL insert trips succeeded"
    return message 

def retrieve_users():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select user_name from users").fetchall()
    return result

def retrieve_trips():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select * from trips").fetchall()
    return result

def remove_trip(trip_id):
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("delete from trips where trip_id = " + trip_id)
    return result

