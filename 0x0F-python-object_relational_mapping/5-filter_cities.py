#!/usr/bin/python3

"""
This module utilizes MySQLdb to execute queries

Author: Bradley Dillion Gilden
Date: 14-09-2023
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    clist = []
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                   INNER JOIN states \
                   ON cities.state_id = states.id \
                   WHERE states.name = %s", (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        clist.append(row[0])
    print(*clist, sep=', ')
    cursor.close()
    conn.close()
