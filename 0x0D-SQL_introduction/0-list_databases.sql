#!/usr/bin/env python3

import mysql.connector

# connect to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
)

# create a cursor object
mycursor = mydb.cursor()

# execute the SHOW DATABASES SQL statement
mycursor.execute("SHOW DATABASES")

# loop through the result set and print each database name
for database in mycursor:
    print(database[0])
