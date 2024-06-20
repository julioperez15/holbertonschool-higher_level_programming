#!/usr/bin/python3
""" This script is safe from SQL injections """

import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    # Create a cursor object
    cur = db.cursor()
    # Execute the SQL query
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
        (state_name_searched,)
    )
    # Fetch the first row from the result set
    row = cur.fetchone()
    # If a row was fetched, print it
    if row is not None:
        print(row)
    # Close the cursor and the database connection
    cur.close()
    db.close()