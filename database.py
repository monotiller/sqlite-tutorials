import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM customers WHERE last_name = 'Smith'") # WHERE allows you to filter results, you can use expressions like you can in for loops and the likes, i.e. age >= 21. You can also use LIKE and wildcards (defined by %) to find things that are similar i.e. %example.com to search email addresses that end in that domain.

items = c.fetchall()
print(items)

# Commit our command
conn.commit()

# Close our connection
conn.close