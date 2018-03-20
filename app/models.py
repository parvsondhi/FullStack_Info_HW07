import sqlite3 as sql
import hashlib, uuid

DATABASE_FILE = 'app.db'

def get_user(conn, user):
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (user, ))
    return c.fetchall()

def hash_pw(pw, salt):
    return hashlib.sha512(pw.encode('utf-8') + salt.encode('utf-8')).hexdigest()

def create_user(user, pw):
    with sql.connect(DATABASE_FILE) as conn:
        if len(get_user(conn, user)) != 0:
            return False
        c = conn.cursor()
        salt = uuid.uuid4().hex
        hashed_password = hash_pw(pw, salt)
        c.execute("INSERT INTO users (email, password, salty) VALUES (?,?,?)", (user, hashed_password, salt))
        conn.commit()
        return True

def check_login(user, pw):
    with sql.connect(DATABASE_FILE) as conn:
        conn.row_factory = sql.Row
        results = get_user(conn, user)
        if len(results) == 0:
            return False
        result = results[0]
        hashed_password = hash_pw(pw, result['salty'])
        return hashed_password == result['password']

def get_users():
    with sql.connect(DATABASE_FILE) as conn:
        conn.row_factory = sql.Row
        c = conn.cursor()
        c.execute("SELECT email FROM users")
        return c.fetchall()

def add_trip(name, dest, email1, email2):
    # SQL statement to insert into database goes here
    with sql.connect(DATABASE_FILE) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO trips (name, dest, email1, email2) VALUES (?,?,?,?)", 
            (name, dest, email1, email2))
        conn.commit()

def get_trips(user):
    with sql.connect(DATABASE_FILE) as conn:
        conn.row_factory = sql.Row
        c = conn.cursor()
        c.execute("SELECT * FROM trips WHERE email1 = ? OR email2 = ?", (user, user))
        trips = []
        for t in c.fetchall():
            otheremail = t['email1']
            if otheremail == user:
                otheremail = t['email2']
            trips.append(dict(trip_id=t['trip_id'],
                name=t['name'],
                dest=t['dest'],
                otheremail=otheremail))
        return trips

def remove_trip(trip_id):
    with sql.connect(DATABASE_FILE) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM trips WhERE trip_id = ?", (trip_id, ))
        conn.commit()
