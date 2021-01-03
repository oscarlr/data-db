#!/bin/env python
import matplotlib
matplotlib.use('Agg')

from tabulate import tabulate
import seaborn as sns
import pandas as pd
import numpy as np

def add_arguments(subparser):
    subparser.add_argument('outdir',metavar='OUTDIR')

def count(conn,table):
    command = "SELECT * FROM %s" % table
    cur = conn.cursor()
    cur.execute(command)
    rows = cur.fetchall()
    return len(rows)

def create_html(conn,html):
    number_of_samples = count(conn,"samples")
    number_of_sequencing_sets = count(conn,"capture")

    header = ["Number of\nsamples","Sequencing\ndatasets"]
    tables = [
        [number_of_samples,number_of_sequencing_sets]
        ]
    
    with open(html,'w') as fh:
        fh.write(tabulate(tables,header,tablefmt='html'))

def get_column_entries(conn,table,column):
    command = "SELECT %s FROM %s" % (column,table)
    cur = conn.cursor()
    cur.execute(command)
    rows = cur.fetchall()
    return [str(r[0]) for r in rows]

def plot(conn,table,cats,outdir):
    for cat in cats:
        entries = pd.DataFrame(np.array(get_column_entries(conn,table,cat)),columns=[cat])
        plt = sns.countplot(data=entries,x=cat)
        if cat == "ethnicity":
            plt.set_xticklabels(["White","Asian","Black or\nAfrican American","Hispanic or\nLatino"])
        fig = plt.get_figure()
        fig.savefig("%s/%s.png" % (outdir,cat)) 
        fig.clf()

def plot_cats(conn,outdir):
    capture_cats = ["probes","dna_source"]
    samples_cats = ["ethnicity","project_name"]
    plot(conn,"capture",capture_cats,outdir)
    plot(conn,"samples",samples_cats,outdir)

def main(args,conn):
    html = "%s/data_db.html" % args.outdir
    create_html(conn,html)

    plot_cats(conn,args.outdir)
