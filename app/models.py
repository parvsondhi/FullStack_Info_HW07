import sqlite3 as sql



def insert_user_data(first_name, last_name, email):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as database:
        cursor = database.cursor()

        cursor.execute('INSERT INTO users (first_name, last_name, email) VALUES (?,?,?)', (first_name, last_name, email))

    database.commit()
    database.close()

def insert_trip(value, trip_title, destination):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO trips (trip_title, destination) VALUES (?,?)", (trip_title, destination))
        cur.execute("INSERT INTO trips (value ) VALUES (?)", (trip_id))
        con.commit()

def retrieve_trips():
    # SQL statement to query database goes here
    with sql.connect("app.db") as database:
        database.row_factory = sql.Row
        cur = database.cursor()
        result = cur.execute("SELECT * FROM trips").fetchall()
