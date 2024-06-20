#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == "__main__":
    try:
        # Extract arguments
        mysql_user = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]

        # Establishing the database connection
        db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                             passwd=mysql_password, db=db_name)

        # Creating a cursor object to interact with the database
        cur = db.cursor()

        # Executing the SQL query
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetching all the rows from the executed query
        rows = cur.fetchall()

        # Iterating through the rows and printing each one
        for row in rows:
            print(row)

        # Closing the cursor and the database connection
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"An error occurred: {e}")
