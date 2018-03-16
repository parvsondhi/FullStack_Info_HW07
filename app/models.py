import sqlite3 as sql

def insert_user(username, password):
	with sql.connect('database.db') as con:
		cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM users WHERE username=?", username)
        if cur.fetchone()>0 return false
		result = cur.execute(
            "INSERT INTO users (username, password)"
            " VALUES (?,?)"
            , )
		con.commit()
        return true

def login(username, password):
	with sql.connect('database.db') as con:
		cur = con.cursor()
        sql = "SELECT COUNT(*) FROM users WHERE (username=? AND password=?)",
        cur.execute(sql, (username, password))
        return (cur.fetchone()>0)
