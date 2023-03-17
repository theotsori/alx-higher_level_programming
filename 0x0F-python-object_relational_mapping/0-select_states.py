#!/usr/bin/python3
"""A script that lists all states from the database
   hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    """ Get mysql username, password, and database from cmd
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    states = cursor.fetchall()
    for state in states:
        print(state)

    db.close()
