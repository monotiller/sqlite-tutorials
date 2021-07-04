import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Drop table
c.execute("DROP TABLE customers")
conn.commit()

# Query the database - ORDER BY
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()
for item in items:
    print(item)

# Commit our command
conn.commit()

# Close our connection
conn.close