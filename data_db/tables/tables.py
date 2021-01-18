#!/bin/env python

projects = """ CREATE TABLE IF NOT EXISTS projects ( 
name text PRIMARY KEY
); """

samples = """ CREATE TABLE IF NOT EXISTS samples (
sample_name text NOT NULL,
project_name text NOT NULL,
ethnicity text,
population text,
PRIMARY KEY (sample_name, project_name),
FOREIGN KEY (project_name) REFERENCES projects (sample_name)
); """

probes = """ CREATE TABLE IF NOT EXISTS probes (
name text PRIMARY KEY,
loci text NOT NULL
); """

capture = """ CREATE TABLE IF NOT EXISTS capture (
data_path text PRIMARY KEY,
sample_name integer NOT NULL,
experiment_name text NOT NULL UNIQUE,
dna_source text NOT NULL,
probes text NOT NULL,
date_added date NOT NULL,
FOREIGN KEY (sample_name) REFERENCES samples (name),
FOREIGN KEY (probes) REFERENCES probes (name)
); """

