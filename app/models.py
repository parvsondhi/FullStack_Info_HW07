import sqlite3 as sql

def insert_trip(trip_name, destination):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO trips (trip_name, destination) VALUES (?,?)",
        (trip_name,destination))
        con.commit()
    return cur.lastrowid

# def retrieve_customers():
#     # SQL statement to query database goes here
#     with sql.connect("app.db") as con:
#         con.row_factory = sql.Row
#         cur = con.cursor()
#         result = cur.execute("SELECT * FROM customers").fetchall()
#     return result
#
# def retrieve_orders():
#     # SQL statement to query database goes here
#     with sql.connect("app.db") as con:
#         con.row_factory = sql.Row
#         cur = con.cursor()
#         result = cur.execute("SELECT * FROM orders").fetchall()
#     return result
#
# ##You might have additional functions to access the database
# def insert_order(name_of_part, manufacturer_of_part, customer_id):
#     with sql.connect("app.db") as con:
#         cur = con.cursor()
#         cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part, customer_id) VALUES (?,?,?)",
#         (name_of_part,manufacturer_of_part,customer_id))
#         con.commit()
#
#
# def insert_address(street_address, city, state, country, zipcode, customer_id):
#     with sql.connect("app.db") as con:
#         cur = con.cursor()
#         cur.execute("INSERT INTO addresses (street_address, city, state, country, zipcode, customer_id) VALUES (?,?,?,?,?,?)",
#         (street_address,city,state,country,zipcode,customer_id))
#         con.commit()
