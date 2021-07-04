import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM customers")
# c.fetchone() # Fetches one record (defaults to last record)
# c.fetchmany() # Fetches as many as you ask for
# c.fetchall() # Fetches everything
print(c.fetchall())

# Commit our command
conn.commit()

# Close our connection
conn.close