import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the database - ORDER BY
c.execute("SELECT * FROM customers ORDER BY last_name")

items = c.fetchall()
print(items)

# Commit our command
conn.commit()

# Close our connection
conn.close