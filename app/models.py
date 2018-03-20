import sqlite3 as sql

def insert_user(username, password):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM users WHERE username=?", [username])
        if cur.fetchone()[0]>0: return False
        result = cur.execute(
            "INSERT INTO users (username, password)"
            " VALUES (?,?)"
            , )
        con.commit()
        return True

def login(username, password):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        sqltext = "SELECT COUNT(*) FROM users WHERE (username=? AND password=?)",
        cur.execute(sqltext, (username, password))
        return (cur.fetchone()[0]>0)

def db_create_trip(name, destination, user1, user2):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        sqltext = ("INSERT INTO trips (name, destination, user1, user2)"
            " VALUES (?, ?)")
        cur.execute(sqltext, (name, destination, user1, user2))
        con.commit()
        return True

def db_delete_trip(id):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM trips WHERE id=?", [id])
        val = cur.fetchone()[0]
        cur.commit()
        return val

def fetch_trips(username):
    response = []
    with sql.connect('database.db') as con:
        cur = con.cursor()
        sqltext = ("SELECT name, destination, user1, user2 "
            "FROM trips "
            "WHERE (user1=? OR user2=?)")
        for rowlist in cur.execute(sqltext, (username, username)):
            row['name'] = rowlist[0]
            row['destination'] = rowlist[1]
            row['user1'] = rowlist[2]
            row['user2'] = rowlist[3]
            response.append(row)
        return response
        

def fetch_other_users(username):
    response = []
    with sql.connct('database.db') as con:
        cur = con.cursor()
        sqltext = ("SELECT username "
            "FROM users "
            "WHERE (username!=?)"
            )
        for rowlist in cur.execute(sqltext, [username]):
            row['username'] = rowlist[0]
            response.append(row)
        return response
