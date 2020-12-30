#!/bin/env python
import os
import sys
import sqlite3
import argparse
import importlib

DB_PATH = "data.db"

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

    parser = argparse.ArgumentParser()
    command = importlib.import_module('.%s' % command_name, "data-db.commands")

    args = parser.parse_args(sys.argv[1:])
    command.main(args)
