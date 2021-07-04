import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a python list with multiple entries
many_customers = [
    ('Wes,' 'Brown', 'wes@example.com'),
    ('Joe', 'Bloggs', 'joe@example.com'),
    ('John', 'Smith', 'john@example.com'),
]

# Create a table
c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers) # ? is used as the placeholder in SQLite

# Commit our command
conn.commit()

# Close our connection
conn.close