# data-db
I need a solution to track all data we generate. Previously, I was doing this with google sheets and docs. Here, I will try to use a SQLite database to keep track of the datasets.
## To do
1. Check if all data paths exists everytime data-db runs

## Quick start
```
git clone https://github.com/oscarlr/data-db
cd data-db
python setup.py install

# data-db <database> <command> <arguments...>
data-db data.db add samples.txt data.txt
data-db data.db stats outdir
```

## Getting existing databases
This private repo, `https://github.com/oscarlr/UofL-Watson-data`, contains the SQL database with datapaths to data generated from the Watson lab. It is updated everytime data gets added to the database. Only users with access to the repo can access the database.

## Tables
```
https://github.com/oscarlr/data-db/blob/main/data_db/tables/tables.py
```

## Adding capture data to db
```
data-db data.db add samples.txt data.txt
```
`data-db add` requires two input files. The first file is a tab-delimited file with the following columns: ``` sample, project_name, ethnicity, population ```. ```name``` and ```project_name```are required. The column  ```ethnicity``` can only contain: ```"American Indian or Alaska Native","Asian", "Black or African American","Hispanic or Latino", "Native Hawaiian or Other Pacific Islander","White"```. 

The second file is a tab delimited file with the following columns: ```data_path, sample_name, dna_source, probes, date_added, sequencing_plex```. All columns are required. 

### Example files:
1. samples.txt: https://github.com/oscarlr/data-db/blob/main/examples/samples.txt
2. data.txt: https://github.com/oscarlr/data-db/blob/main/examples/data.txt

## Generating stats
```
data-db data.db stats outdir
```
`data-db stats` only requires an output directory and outputs an html file and plots with stats from the tables. Here's an example: https://oscarlr.github.io/projects
