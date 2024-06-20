#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    # Creates a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("""SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC""",
                (state_name,))

    # Fetch all rows from the result
    rows = cur.fetchall()

    # Create a list of city names,
    city_names = []
    for row in rows:
        if row[0] not in city_names:
            city_names.append(row[0])

    # Print city names on the same line, separated by commas
    print(", ".join(city_names))

    # Close the cursor and the database connection
    cur.close()
    db.close()