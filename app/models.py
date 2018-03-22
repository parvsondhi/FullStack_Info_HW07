import sqlite3 as sql
import hashlib
import uuid

def create_user(username, password, first, last):
    # SQL statement to insert into database goes here
    
    with sql.connect("app.db") as con:
        if len(get_user(con, username)) != 0:
            return False
        cur = con.cursor()			#access the the database you just connected to
#primary key is automatically added by normal incrementation. If you want otherwise, u need to manually add it
        cur.execute("INSERT INTO users (email_id, password, first_name, last_name) VALUES (?, ?, ?, ?)"
    	   , (username, password, first, last))
        con.commit()
        return True
    
def insert_trip(name, location, email_id1, email_id2):
    # SQL statement to insert into database goes here
    if name == ""  or name == " " or location == " " or location == "" or email_id1 == "" or email_id2 == "":
        return False
    with sql.connect("app.db") as con:
        cur = con.cursor()          #access the the database you just connected to
#primary key is automatically added by normal incrementation. If you want otherwise, u need to manually add it
        cur.execute("INSERT INTO trips (name, location, email_id1, email_id2) VALUES (?, ?, ?, ?)"
            , (name, location, email_id1, email_id2))
        con.commit()

def delete_trip(trip_id):
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row       #Ensuring u r receiving data as actual row objects
        cur = con.cursor()
        cur.execute("DELETE FROM trips WHERE trip_id = ?", (trip_id, ))   #another option is fetchone()
        con.commit()   

def retrieve_trips(username):

    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        results = cur.execute("SELECT * FROM trips WHERE email_id1 = ? OR email_id2 = ?", (username, username)).fetchall()

        trips = []

        for res in results:
            if res['email_id1'] == username:
                friend = res['email_id2']
            else:
                friend = res['email_id1']
            trips.append(dict(trip_id = res['trip_id'], name = res['name'], location = res['location'], friend = friend))

        return trips

def authenticate_user(username, password):
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        users = get_user(con, username)
        if username == None or password == None:
            return False
        if len(users) == 0:
            return False

        user = users[0]
        
        return user['password'] == password


def get_user(con, email_id):

    cur = con.cursor()
    result = cur.execute("SELECT * FROM users WHERE email_id = ?", (email_id, )).fetchall()
    return result

def get_users():

    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        results = cur.execute("SELECT email_id FROM users").fetchall()
        return results