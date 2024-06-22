#!/usr/bin/python3
"""write a script that takes in arguments and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time, write one
that is safe from MySQL injections!"""
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
        name=%s"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
