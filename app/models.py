import sqlite3 as sql

def insert_user(username, password):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM users WHERE username=?", [username])
        if cur.fetchone()[0]>0 return False
        result = cur.execute(
            "INSERT INTO users (username, password)"
            " VALUES (?,?)"
            , )
        con.commit()
        return True

def login(username, password):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        sql = "SELECT COUNT(*) FROM users WHERE (username=? AND password=?)",
        cur.execute(sql, (username, password))
        return (cur.fetchone()[0]>0)

def create_trip(name, destination, user1, user2):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        sql = ("INSERT INTO trips (name, destination, user1, user2)"
            " VALUES (?, ?)")
        cur.execute(sql, (name, destination, user1, user2))
        con.commit()
        return True

def delete_trip(id):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM trips WHERE id=?", [id])
        val = cur.fetchone()[0]
        cur.commit()
        return val

