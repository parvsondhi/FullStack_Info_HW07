import sqlite3 as sql

def retrieve_users():
    # SQL statement to query database goes here
    with sql.connect("app.db") as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        result = cur.execute("select users.userid, users.username from users").fetchall()
    return result

def retrieve_trips(user):
    # SQL statement to query database goes here
    with sql.connect("app.db") as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        result = cur.execute("select t.id, t.tripname, t.destination from trips as t, user_to_trip as ut where t.id = ut.tripid and ut.userid =" + str(user)).fetchall()
    return result


##You might have additional functions to access the database
def signup(username, password):
    with sql.connect("app.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users(username, password) VALUES (?, ?)", (username, password))
        userid = cur.execute('SELECT last_insert_rowid()').fetchone()[0]
        conn.commit()
    return userid

def add_trip(tripname, destination, user1, user2):
    with sql.connect("app.db") as conn:
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO trips(tripname, destination, userid_1, userid_2) VALUES (?, ?, ?, ?)", (tripname, destination, user1, user2))
        tripid = cur.execute('SELECT last_insert_rowid()').fetchone()[0]
        cur.execute("INSERT INTO user_to_trip(userid, tripid) VALUES (?, ?)", (user1, tripid))
        cur.execute("INSERT INTO user_to_trip(userid, tripid) VALUES (?, ?)", (user2, tripid))
        conn.commit()


def remove_trip(tripid):
    with sql.connect("app.db") as conn:
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("DELETE FROM user_to_trip WHERE tripid =" + str(tripid))
        cur.execute("DELETE FROM trips WHERE id =" + str(tripid))
        conn.commit()