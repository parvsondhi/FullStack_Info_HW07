import sqlite3 as sql
import sys

# def insert_data():
#     # SQL statement to insert into database goes here
    
def insert_trip(trip_title, destination, friend):
    # SQL statement to insert into database
    with sql.connect('app.db') as con:
        cur = con.cursor() # creating cursor
        cur.execute("INSERT INTO trip (trip_title, destination, friend) VALUES (?,?,?)", (trip_title, destination, friend))
        con.commit() # commit = save to database
        trip_id = cur.lastrowid
    return int(trip_id)

def retrieve_trips(username): 
    # SQL statement to query database goes here
    with sql.connect('app.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor() # creating cursor
        # not sure if below sql statement is correctly passing parameters in
        result = cur.execute("SELECT trip.trip_title, trip.destination, trip.trip_id FROM trip INNER JOIN trip_user ON trip.trip_id = trip_user.trip_id WHERE trip_user.uid = (?) OR trip_user.friend_id = (?)", (username, username)).fetchall() 
        print(result, file=sys.stderr)
    return result

# def insert_order (name_of_part, manufacturer_of_part):
#     with sql.connect('database.db') as con:
#         cur = con.cursor() 
#         cur.execute("INSERT INTO 'orders' (name_of_part, manufacturer_of_part) VALUES (?,?)", (name_of_part, manufacturer_of_part))
#         con.commit()
#     return cur.lastrowid

# def retrieve_orders():
#     # SQL statement to query database goes here
#     with sql.connect('database.db') as con:
#         con.row_factory = sql.Row
#         cur = con.cursor() # creating cursor
#         result = cur.execute("SELECT orders.name_of_part, orders.manufacturer_of_part, customer_orders.customer_id FROM 'orders' INNER JOIN 'customer_orders' ON orders.order_id=customer_orders.order_id;").fetchall()
#         print(result)
#     return result

def insert_trip_user(trip_id, uid, friend_id):
    with sql.connect('app.db') as con:
        cur = con.cursor() 
        cur.execute("INSERT INTO 'trip_user' (trip_id, uid, friend_id) VALUES (?,?,?)", (trip_id, uid, friend_id))
        con.commit()

def getID(current_user):
    with sql.connect('app.db') as con:
        con.row_factory = lambda cursor, row: row[0]
        cur = con.cursor() 
        result = cur.execute("SELECT uid FROM user WHERE username = (?)", [current_user]).fetchone()
    return result

def retrieve_friends(current_user):
    with sql.connect('app.db') as con:
        con.row_factory = lambda cursor, row: row[0]
        cur = con.cursor() # creating cursor
        result = cur.execute("SELECT username FROM user WHERE username != (?)", [current_user]).fetchall()
        # result = cur.execute("SELECT trip.trip_title, trip.destination FROM trip INNER JOIN trip_user ON trip.trip_id = trip_user.trip_id WHERE trip_user.uid = (?)", [username]).fetchall() 
        print(result, file=sys.stderr)
    return result
##You might have additional functions to access the database

def delete_trip(trip_id):
    with sql.connect('app.db') as con:
        cur = con.cursor() 
        cur.execute("DELETE FROM trip_user WHERE trip_id = (?)", (trip_id))
        cur.execute("DELETE FROM trip WHERE trip_id = (?)", (trip_id))
        con.commit()