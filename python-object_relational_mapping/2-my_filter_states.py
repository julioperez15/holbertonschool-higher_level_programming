#!/usr/bin/python3
"""script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa
where name matches the argument."""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
        )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE\
        BINARY name LIKE '{}'".format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
