import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the database - ORDER BY
c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 3") # So we can use this where we vaguely remember someone's surname but we might remember the rowid

items = c.fetchall()
print(items)

# Commit our command
conn.commit()

# Close our connection
conn.close