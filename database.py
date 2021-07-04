import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT rowid, * FROM customers") # rowid is how you access the id of each entry, so instead of searching for "Joe Bloggs" you can just call key 3 for example

items = c.fetchall()
print(items)

# Commit our command
conn.commit()

# Close our connection
conn.close