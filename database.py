import sqlite3

# Query the DB and return all records
def show_all():
    # Connect to database
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()

    # Query the database - ORDER BY
    c.execute("SELECT rowid, * FROM customers")
    
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command
    conn.commit()

    # Close our connection
    conn.close()

# Add a new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    conn.commit()
    conn.close()

# Add many records to a table
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

# Delete a record from the table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

# Lookup with WHERE
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.close()