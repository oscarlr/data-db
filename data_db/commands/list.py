#!/bin/env python
import sys
import sqlite3

from data_db.common import add_sql_entries

#DB_PATH = "data.db"

def add_arguments(subparser):
    pass

def list_datasets(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM samples")

    header = list(map(lambda x: x[0], cur.description))
    rows = cur.fetchall()

    print("%s" % "\t".join(header))
    for row in rows:
        print("%s" % "\t".join(map(str,row)))

def main(args,conn):
    list_datasets(conn)

