#!/usr/bin/python3
"""
Script that lists all cities of a given state
"""

import sys
import MySQLdb


def list_cities_by_state():
    """
    Lists all cities of a given state from the db
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306)
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM states\
                JOIN cities ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (state,))

    results = cur.fetchall()

    print(", ".join(city[0] for city in results))
    #for row in results:
    #    print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    list_cities_by_state()
