#!/bin/env python

projects = """ CREATE TABLE IF NOT EXISTS projects ( 
id integer PRIMARY KEY, 
name text NOT NULL
); """

samples = """ CREATE TABLE IF NOT EXISTS samples (
id integer PRIMARY KEY,
name text NOT NULL,
project_id integer NOT NULL
); """

capture = """ CREATE TABLE IF NOT EXISTS capture (
id integer PRIMARY KEY,
sample_id integer NOT NULL,
probes text NOT NULL,
data_path text NOT NULL,
date_added date NOT NULL,
sequence_plex integer NOT NULL,
number_reads integer NOT NULL,
number_bases integer NOT NULL
); """

