#!/bin/env python
import sys
import sqlite3

from data_db.common import add_sql_entries

#DB_PATH = "data.db"

def add_arguments(subparser):
    subparser.add_argument('samples',metavar='SAMPLES',help='samples fofn')
    subparser.add_argument('data',metavar='DATA',help='data fofn')

def check_data_header(header,entries):
    for entry in entries:
        if entry not in header:
            sys.exit("%s not found" % entry)

def check_table(conn,table,column,value):
    cur = conn.cursor()
    command = "SELECT * FROM %s WHERE %s=?" % (table,column)
    cur.execute(command, (value,))
    rows = cur.fetchall()
    if len(rows) == 0:
        sys.exit("%s not found in table %s column %s" % (value,table,column))

def check_ethnicity(ethnicity):
    ethnicities = ["American Indian or Alaska Native","Asian",
                   "Black or African American","Hispanic or Latino",
                   "Native Hawaiian or Other Pacific Islander","White"]
    if ethnicity not in ethnicities:
        print "Pick an ethnicity from %s" % ",".join(ethnicities)
        sys.exit("%s not allowed" % ethnicity)

def add_samples(samplefofn,conn):
    print "Going through %s..." % samplefofn
    samples = []
    possible_entries = ["sample","project","ethnicity","population"]
    with open(samplefofn,'r') as samplefofh:
        for i,line in enumerate(samplefofh):
            line = line.rstrip().split('\t')
            if i == 0:
                header = line
                check_data_header(header,["sample","project"])
                continue
            vals = []
            for possible_entry in possible_entries:
                if possible_entry == "project":
                    check_table(conn,"projects","name",line[header.index(possible_entry)])
                if possible_entry == "ethnicity":
                    check_ethnicity(line[header.index(possible_entry)])
                if possible_entry in header:
                    vals.append(line[header.index(possible_entry)])
                else:
                    vals.append("None")
            vals = tuple(vals)
            samples.append(vals)
    sql = ''' INSERT OR IGNORE INTO samples (name,project_name,ethnicity,population) 
              VALUES(?,?,?,?) '''
    add_sql_entries(conn,samples,sql)


def add_capture_data(datafn,conn):
    print "Going through %s..." % datafn
    datapaths = []
    entries = ["data_path","sample_name","experiment_name","dna_source",
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
                if entry == "sample_name":
                    check_table(conn,"samples","name",line[header.index(entry)])
                vals.append(line[header.index(entry)])
            vals = tuple(vals)
            datapaths.append(vals)
    sql = ''' INSERT INTO capture (data_path,sample_name,experiment_name,dna_source,probes,date_added,sequencing_plex)
              VALUES(?,?,?,?,?,?,?) '''
    add_sql_entries(conn,datapaths,sql)
                
def main(args,conn):
    add_samples(args.samples,conn)
    add_capture_data(args.data,conn)

