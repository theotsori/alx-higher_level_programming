#!/usr/bin/python3
""" filter states by user input
"""
import MySQLdb
import sys

if __name__ == '__main__':
    """ Get command line arguments
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=mysql_user,
                           passwd=mysql_password,
                           db=db_name)

    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    conn.close()
