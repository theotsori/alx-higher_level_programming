#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='Theowein@23',
                         db='hbtn_0e_0_usa')

    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    states = cursor.fetchall()
    for state in states:
        print(state)

    db.close()
