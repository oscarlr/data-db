#!/bin/env python

projects = """ CREATE TABLE IF NOT EXISTS projects (
project_id integer PRIMARY KEY,
name text NOT NULL
); """

samples = """ CREATE TABLE IF NOT EXISTS samples (
sample_id integer PRIMARY KEY,
name text NOT NULL
project_id integer NOT NULL
); """

print samples
