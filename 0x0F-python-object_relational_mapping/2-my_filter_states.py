#!/usr/bin/python3

"""
This module utilizes MySQLdb to execute queries

Author: Bradley Dillion Gilden
Date: 14-09-2023
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}';".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
