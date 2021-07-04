import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Update records
c.execute("""UPDATE customers SET first_name = 'Bob'
            WHERE last_name = 'Smith'
""")

conn.commit()

# Query the database
c.execute("SELECT * FROM customers")

items = c.fetchall()
print(items)

# Commit our command
conn.commit()

# Close our connection
conn.close