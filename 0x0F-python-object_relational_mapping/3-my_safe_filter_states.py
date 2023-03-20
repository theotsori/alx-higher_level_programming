#!/usr/bin/python3
""" Script that takes in args and displays all values
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
      host="localhost",
      port=3306,
      user=sys.argv[1],
      passwd=sys.argv[2],
      database=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY name = %s", sys.argv[4])

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
