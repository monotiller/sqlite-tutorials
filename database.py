import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text
)""")

# The SQLite datatypes:
# NULL
# INTEGER
# REAL
# TEXT
# BLOB - Stores data exactly how it is, i.e. images, audio, video

# Commit our command
conn.commit()

# Close our connection
conn.close