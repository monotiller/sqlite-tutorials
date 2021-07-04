import database

# Add a record to the database
database.add_one(input("Name: "), input("Surname: "), input("Email: "))

# Show all the records
database.show_all()