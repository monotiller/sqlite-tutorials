import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Delete Records
c.execute("DELETE from customers WHERE rowid = 6")

conn.commit()

# Query the database
c.execute("SELECT * FROM customers")

items = c.fetchall()
print(items)

# Commit our command
conn.commit()

# Close our connection
conn.close