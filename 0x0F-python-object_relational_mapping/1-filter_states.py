#!/usr/bin/python3

""" Script that lists all states with a name 'N'
"""
import MySQLdb
import sys

if __name__ == '__main__':
    """ script will take three args from the cmd
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=mysql_user,
                           passwd=mysql_password,
                           db=db_name)

    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
