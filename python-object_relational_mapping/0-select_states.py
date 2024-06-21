#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],          # Your MySQL username
        passwd=sys.argv[2],        # Your MySQL password
        db=sys.argv[3]             # The database name
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cur.close()
    db.close()
