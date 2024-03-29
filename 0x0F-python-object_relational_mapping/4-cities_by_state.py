#!/usr/bin/python3
"""script that lists all cities from database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cr = db.cursor()
    myQuery = " ".join([
        "SELECT cities.id, cities.name, states.name FROM cities",
        "INNER JOIN states ON states.id = cities.state_id",
        "ORDER BY cities.id"
        ])
    cr.execute(myQuery)
    res = cr.fetchall()
    for rows in res:
        print(rows)
    cr.close()
    db.close()
