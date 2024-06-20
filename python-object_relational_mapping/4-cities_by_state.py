#!/usr/bin/python3
"""This script lists all cities from a given MySQL database."""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    # Creates a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC""")

    # Fetch all rows from the result
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()