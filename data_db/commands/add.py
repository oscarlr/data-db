#!/bin/env python
import sys
import sqlite3

from data_db.common import add_sql_entries

DB_PATH = "data.db"

def add_arguments(subparser):
    subparser.add_argument('samples',metavar='SAMPLES',help='samples fofn')
    subparser.add_argument('data',metavar='DATA',help='data fofn')

def check_sample_header(header):
    if "sample" not in header:
        sys.exit("%s does not contain sample" % samplefofn)
    if "project" not in header:
        sys.exit("%s does not contain project" % samplefofn)
    if "ethnicity" not in header:
        print "%s does not contain ethnicity. Continuing... " % samplefofn

def add_samples(samplefofn,conn):
    samples = []
    possible_entries = ["sample","project","ethnicity","population"]
    with open(samplefofn,'r') as samplefofh:
        for i,line in enumerate(samplefofh):
            line = line.rstrip().split('\t')
            if i == 0:
                header = line
                check_sample_header(header)
                continue
            vals = []
            for possible_entry in possible_entries:
                if possible_entry in header:
                    vals.append(line[header.index(possible_entry)])
                else:
                    vals.append("None")
            vals = tuple(vals)
            samples.append(vals)
    sql = ''' INSERT OR IGNORE INTO samples (name,project_name,ethnicity,population) 
              VALUES(?,?,?,?) '''
    add_sql_entries(conn,samples,sql)

def check_data_header(header,entries):
    for entry in entries:
        if entry not in header:
            sys.exit("%s not found" % entry)

def add_data(datafn,conn):
    datapaths = []
    entries = ["data_path","sample_name","dna_source",
               "probes","date_added","sequencing_plex"]
    with open(datafn,'r') as datafh:
        for i,line in enumerate(datafh):
            line = line.rstrip().split('\t')
            if i == 0:
                header = line
                check_data_header(header,entries)
                continue
            vals = []
            for entry in entries:
                vals.append(line[header.index(entry)])
            vals = tuple(vals)
            datapaths.append(vals)
    sql = ''' INSERT INTO capture (data_path,sample_name,dna_source,probes,date_added,sequencing_plex)
              VALUES(?,?,?,?,?,?) '''
    add_sql_entries(conn,datapaths,sql)
                
def main(args,conn):
    add_samples(args.samples,conn)
    add_data(args.data,conn)

