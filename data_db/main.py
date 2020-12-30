#!/bin/env python
import os
import sys
import sqlite3
import argparse
import importlib

from sqlite3 import Error

DB_PATH = "data.db"

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_sql_entries(conn,entries,sql):
    for entry in entries:
        cur = conn.cursor()
        cur.execute(sql,entry)
        conn.commit()

def add_probes_entries(conn):
    probes = [
        ("V4","IGHV,IGL,TCRA,TCRB"),
        ("V3","IGHV")
    ]
    sql = ''' INSERT INTO probes (name,loci)
              VALUES(?,?) '''
    add_sql_entries(conn,probes,sql)

def add_project_entries(conn):
    projects = [
        ("Wayne-Flu",),
        ("Boyd-Healthy",),
        ("STEMCELL",),
        ("1KG",),
        ("GIAB",)
    ]
    sql = ''' INSERT INTO projects (name)
              VALUES(?) '''
    add_sql_entries(conn,projects,sql)

def add_tables():
    from data_db.tables.tables import samples,capture,projects,probes

    tables = [samples,capture,projects,probes]
    
    conn = sqlite3.connect(DB_PATH)

    for table in tables:
         create_table(conn,table)

    add_probes_entries(conn)
    add_project_entries(conn)

    conn.close()
    
def create_db():
    conn = sqlite3.connect(DB_PATH)
    conn.close()

def main():
    commands = [
        "stats"
    ]

    if len(sys.argv) < 2:
        sys.exit("Please run one of the following commands: \n%s" % "\n".join(commands))

    command_name = sys.argv[1]

    if command_name not in commands:
        sys.exit("Please run one of the following commands: \n%s" % "\n".join(commands))

    if not os.path.isfile(DB_PATH):
        create_db()

    add_tables()
    # parser = argparse.ArgumentParser()
    # command = importlib.import_module('.%s' % command_name, "data-db.commands")

    # args = parser.parse_args(sys.argv[1:])
    # command.main(args)
