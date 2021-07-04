import sqlite3

# Query the DB and return all records
def show_all():
    # Connect to database
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()

    # Query the database - ORDER BY
    c.execute("SELECT rowid, * FROM customers")
    
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command
    conn.commit()

    # Close our connection
    conn.close