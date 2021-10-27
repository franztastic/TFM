
#PAS 1.

#Concatena fitxers tsv i agafa sel·lecciona només la primera mostra.
import os
from glob import glob 
import pandas as pd
import csv
import sys
import numpy

vpfclass_directory = '/Users/lauratriginer/Documentos/Màster en Enginyeria Biomèdica/tfm/practica/VPF_Class Classified'
os.chdir(vpfclass_directory)

filename = 'merged_family_to_vpf_output.tsv'

with open(filename,'w') as singleFile:
    first_tsv = True 
    for tsv in glob('*.tsv'):
        if tsv == filename:
            pass
        else:
            header = True 
            for line in open(tsv,'r'):
                if first_tsv and header:
                    singleFile.write(line)
                    first_tsv=False
                    header = False
                elif header:
                    header = False
                else:
                    singleFile.write(line)
    singleFile.close()

    #PAS 2. CERCA DUPLICATS

with open (filename, 'r') as merged_class:
    with open ('merged_family_vpf_output.csv', 'w' ) as filt_vpf:
        merged_file = pd.read_csv(merged_class, sep='\\t', engine ='python')
        pd.set_option('display.max_rows',None)
        pd.set_option('display.max_colwidth',None)
        #pd.set_option('display.max_columns',None)
        unic_class = pd.DataFrame.drop_duplicates(merged_file, subset='virus_name', keep='first')
        del unic_class['virus_hit_score']
        writer_filt=csv.writer(filt_vpf,escapechar='\t',quoting=csv.QUOTE_NONE, lineterminator='\r')
        writer_filt.writerow([unic_class])
            
  #  print('Porcentaje de muestras clasificadas de Baltimore por VPF_CLASS: ' + str(class_balt/num_samples*100)+ '%')
  # print(class_balt)

