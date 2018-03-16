import sqlite3 as sql

# I think retrieve trips will be better
def retrieve_trips():

# change name to insert_trip
def insert_trip():
    

# remove trip column from the table trips
def delete_trip():
    # DELETE FROM table_name WHERE some_column=some_value;
    # ex: Delete from users where name = ‘eric’

# change name to retrieve_user
# retrieve all user for the dropdown in the "creat"
#def retrieve_friends():
def retrieve_user():
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select * from users").fetchall()
    return result

# change name to insert_user
# def create_user():
def insert_user(username, password, first_name, last_name):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO user (username, password, first_name, last_name) VALUES (?,?,?,?)", (username, password, first_name, last_name))
        con.commit()
    return cur.lastrowid

def google_maps():
