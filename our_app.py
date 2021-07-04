import database

# Add a record to the database
# database.add_one(input("Name: "), input("Surname: "), input("Email: "))

# # Add many records
# stuff = [
#     ('Brenda', 'Smitherton', 'brenda@example.com'),
#     ('Joshua', 'Raintree', 'josh@example.com'),
# ]
# database.add_many(stuff)

# Show all the records
database.show_all()

# Lookup email address record
database.email_lookup(str(input("Email to search: ")))

# Delete a record - rowid has to be a string
# database.delete_one(str(input("Delete id: ")))