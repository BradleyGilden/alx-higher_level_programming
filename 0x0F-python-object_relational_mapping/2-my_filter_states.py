#!/usr/bin/python3

"""
This module utilizes MySQLdb to execute queries

Author: Bradley Dillion Gilden
Date: 14-09-2023
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    query = "SELECT * FROM states WHERE BINARY name = '{}';"
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    cursor.execute(query.format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
