import sqlite3 as sql

def retrieve_customers():
    conn = sql.connect('app.db')
    c = conn.cursor()
    results = []
    c.execute("SELECT * FROM customer")
    for row in c.execute('SELECT * FROM customer'):
        customer = {}
        customer["customer_id"] = row[0]
        customer["first_name"] = row[1]
        customer["last_name"] = row[2]
        customer["company"] = row[3]
        customer["email"] = row[4]
        customer["phone"] = row[5]
        results.append(customer)
    conn.close()
    return results
def retrieve_orders():
    conn = sql.connect('app.db')
    c = conn.cursor()
    results = []
    for row in c.execute('SELECT * FROM purchase_order'):
        order = {}
        order["order_id"] = row[0]
        order["name_of_part"] = row[1]
        order["manufacturer_of_part"] = row[2]
        results.append(order)
    conn.close()
    return results
def insert_customer (first_name, last_name, company, email, phone):
    conn = sql.connect('app.db')
    c = conn.cursor()
    customer_id = find_max_customer_id() + 1
    c.execute("INSERT INTO customer VALUES (%d, '%s', '%s', '%s', '%s', '%s')" %(customer_id, first_name, last_name, company, email, phone))
    conn.commit()
    conn.close()
def insert_order (name_of_part, manufacturer_of_part):
    conn = sql.connect('app.db')
    c = conn.cursor()
    order_id = find_max_order_id() + 1
    c.execute("INSERT INTO purchase_order VALUES (%d, '%s', '%s')" %(order_id, name_of_part, manufacturer_of_part))
    conn.commit()
    conn.close()
def insert_customer_order (id, order_id, customer_id):
    conn = sql.connect('app.db')
    c = conn.cursor()
    c.execute("INSERT INTO customer_order VALUES (%d, %d, %d)" %(id, order_id, customer_id))
    conn.commit()
    conn.close()
def insert_address (id, street_address, city, state, country, zip_code, customer_id):
    conn = sql.connect('app.db')
    c = conn.cursor()
    c.execute("INSERT INTO address VALUES (%d, '%s', '%s', '%s', '%s', '%s',%d)" %(id, street_address, city, state, country, zip_code, customer_id))
    conn.commit()
    conn.close()

def find_max_customer_id ():
    # conn = sql.connect('app.db')
    # c = conn.cursor()
    # c.execute("SELECT MAX(customer_id) FROM customer")
    # conn.commit()
    # conn.close()
    conn = sql.connect('app.db')
    c = conn.cursor()
    results = 0
    for row in c.execute('SELECT MAX(customer_id) FROM customer'):
        if row[0] == None:
            results = 0
        else:
            results = row[0]
    conn.close()
    return results

def find_max_order_id ():
    # conn = sql.connect('app.db')
    # c = conn.cursor()
    # c.execute("SELECT MAX(customer_id) FROM customer")
    # conn.commit()
    # conn.close()
    conn = sql.connect('app.db')
    c = conn.cursor()
    results = 0
    for row in c.execute('SELECT MAX(order_id) FROM purchase_order'):
        if row[0] == None:
            results = 0
        else:
            results = row[0]
    conn.close()
    return results

print find_max_customer_id()

# insert_customer(12313,'br','rb','asf','asdfsa','123123')
# retrieve_customers()
# insert_order(12313,'br','rb')
# retrieve_orders()

