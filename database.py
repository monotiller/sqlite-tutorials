import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM customers")

items = c.fetchall()

for item in items:
    print(item) # Prints out each entry as a tuple, which means you can do formating like this:
    print(f"First name: {item[0]}")
    print(f"Last name: {item[1]}")
    print(f"Email: {item[2]}")

# Commit our command
conn.commit()

# Close our connection
conn.close