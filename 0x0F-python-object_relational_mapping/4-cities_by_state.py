#!/usr/bin/python3

"""
Script that lists all cities from the database
"""

import sys
import MySQLdb


def list_cities():
    """
    Lists all cities from the database
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306)

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM\
                cities INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    list_cities()
