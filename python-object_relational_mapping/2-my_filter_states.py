#!/usr/bin/python3
"""script that takes an argument and displays all values in the states table"""


import MySQLdb
import sys

if __name__ == "__main__":
    """ establishes a connection to the database """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BYE id ASC"
    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # Close the cursor and database connection outside of the loop
    cursor.close()
    db.close()