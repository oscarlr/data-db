#!/bin/env python

projects = """ CREATE TABLE IF NOT EXISTS projects ( 
name text PRIMARY KEY
); """

samples = """ CREATE TABLE IF NOT EXISTS samples (
name text text NOT NULL,
project_name text NOT NULL,
PRIMARY KEY (name, project_name),
FOREIGN KEY (project_name) REFERENCES projects (name)
); """

probes = """ CREATE TABLE IF NOT EXISTS probes (
name text PRIMARY KEY,
loci text NOT NULL
); """

capture = """ CREATE TABLE IF NOT EXISTS capture (
data_path text PRIMARY KEY,
sample_name integer NOT NULL,
probes text NOT NULL,
date_added date NOT NULL,
sequencing_plex integer NOT NULL,
number_reads integer NOT NULL,
number_bases integer NOT NULL,
FOREIGN KEY (sample_name) REFERENCES samples (name),
FOREIGN KEY (probes) REFERENCES probes (name)
); """

