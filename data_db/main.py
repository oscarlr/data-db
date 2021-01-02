#!/bin/env python
import os
import sys
import sqlite3
import argparse
import importlib

from sqlite3 import Error

from data_db.common import add_sql_entries

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

def add_probes_entries(conn):
    probes = [
        ("V4","IGHV,IGL,TCRA,TCRB"),
        ("V3","IGHV")
    ]
    sql = ''' INSERT OR IGNORE INTO probes (name,loci)
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
    sql = ''' INSERT OR IGNORE INTO projects (name)
              VALUES(?) '''
    add_sql_entries(conn,projects,sql)

def add_tables(conn):
    from data_db.tables.tables import samples,capture,projects,probes

    tables = [samples,capture,projects,probes]
    
    for table in tables:
         create_table(conn,table)

    add_probes_entries(conn)
    add_project_entries(conn)

    
def open_db(db_path):
    if not os.path.isfile(db_path):
        print "Creating %s..." % db_path
    conn = sqlite3.connect(db_path)
    return conn

def main():
    commands = [
        "stats",
        "add"
    ]

    if len(sys.argv) < 3:
        sys.exit("Please run one of the following commands: \n%s" % "\n".join(commands))

    db_path = sys.argv[1]
    command_name = sys.argv[2]

    if command_name not in commands:
        sys.exit("Please run one of the following commands: \n%s" % "\n".join(commands))


    conn = open_db(db_path)

    add_tables(conn)

    parser = argparse.ArgumentParser(description='')
    subparsers = parser.add_subparsers()

    command = importlib.import_module('.%s' % command_name, "data_db.commands")
    subparser = subparsers.add_parser(command_name)
    command.add_arguments(subparser)


    args = parser.parse_args(sys.argv[2:])
    command.main(args,conn)

    conn.close()
