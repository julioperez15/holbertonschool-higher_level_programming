#!/usr/bin/python3
"""script that takes an argument and displays all values in the states table"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ establishes a connection to the database """
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
        cursor.close()
        db.close()