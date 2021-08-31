
from abc import abstractstaticmethod
from datetime import date
import os
import sys
import pandas as pd
import numpy as np
import csv
import re

from pandas.io.parsers import read_csv 

blast_db_csv = "/Users/lauratriginer/blastdb/protseq_gen_fam_refseq.csv"

contgenus=0
contfamily=0

with open ('blastx_best_hit_noblank.csv','r') as blastx_scnd_filt:
        with open ('class_blastx_fam_gen.csv','w') as add_fam_gen:
            with open ('genus_classif.csv', 'w') as genus_class:
                with open('fam_classif.csv','w') as fam_class:
                    for line in blastx_scnd_filt:
                        if 'Query=' in line:
                            writer = csv.writer(add_fam_gen, escapechar='\t', quoting=csv.QUOTE_NONE, lineterminator='\r')
                            writer.writerow([line]) 
                        else:
                            gen_writer=csv.writer(genus_class, escapechar='\t',quoting=csv.QUOTE_NONE, lineterminator='\r')
                            fam_writer=csv.writer(fam_class, escapechar='\t',quoting=csv.QUOTE_NONE, lineterminator='\r')
                            accession_name = str(line.split('  ')[0])
                            writer.writerow([line])
                            with open (blast_db_csv,'r') as blast_db: #columna 1 #accession columna 4, genus, columna 5 familia.
                                for rows in blast_db:
                                    accession_db=str(rows.split(',')[0])
                                    if accession_db in accession_name:
                                        writer=csv.writer(add_fam_gen,escapechar='\t', quoting=csv.QUOTE_NONE, lineterminator='\r' )
                                        genus=rows.split(',')[3]
                                        if not genus:
                                            genus='genus no info'
                                            writer.writerow([genus])
                                            gen_writer.writerow([genus])
                                        else:
                                            writer.writerow([genus])
                                            contgenus=contgenus+1
                                            gen_writer.writerow([genus])
                                            
                                        family=rows.split(',')[4]
                                        if not family:
                                            family='family no info'
                                            writer.writerow([family])
                                            fam_writer.writerow([family])
                                        else:
                                            writer.writerow([family])
                                            fam_writer.writerow([family])
                                            contfamily=contfamily+1

print('se han clasificado ' +str(contgenus) +' muestras según su género ')
print('se han clasificado ' +str(contfamily) +' muestras según su familia')