import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute ("INSERT INTO customers VALUES ('Leah', 'Smith', 'leah@example.com')")

# Commit our command
conn.commit()

# Close our connection
conn.close