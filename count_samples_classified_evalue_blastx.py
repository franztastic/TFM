
# Calculates the number of samples classified by blastx given an e-value and onlu keeps the best hit for each Query


from datetime import date
import os
import sys
import pandas as pd
import numpy as np
import csv
import re 


blastx_file = "/Users/lauratriginer/resultats_gen_fam_AVs_Viral_sequences.csv"

#llegeix classificats i calcula nº de mostres diferents classificades
with open (blastx_file,'r') as blastx_classified:
    with open ('blastx_filt_samples_SEQUENCES.csv', 'w', newline='') as filter_samples:
        for line in blastx_classified:
            if line.startswith('Query='):
                writer = csv.writer(filter_samples, escapechar='\t', quoting=csv.QUOTE_NONE, lineterminator='\r')
                writer.writerow([line]) 
            elif line.startswith('YP_'):
                evalue= line.split('    ')[-1]
                evalue = float(evalue)
                if evalue <= 1e-10:
                    writer = csv.writer(filter_samples, escapechar='\t',quoting = csv.QUOTE_NONE, lineterminator='\r')
                    writer.writerow([line])                   

firstYP=0
previous_line = 'a'
control_line='a'
num_mostres_class=0
with open ('blastx_filt_samples_SEQUENCES.csv','r') as blastx_first_class:
    with open ('blastx_best_hit.csv','w',newline='') as second_filter:
        for lines in blastx_first_class:
            if lines.startswith('Query=') and (("Query" in previous_line) or previous_line=='a'):
                writer = csv.writer(second_filter, escapechar='\t', quoting=csv.QUOTE_NONE)
                writer.writerow([lines])
                firstYP=0
            elif lines.startswith('YP_') and firstYP==0:
                writer = csv.writer(second_filter, escapechar =' ', quoting = csv.QUOTE_NONE)
                writer.writerow([lines])
                firstYP=1
                control_line='b'
                num_mostres_class=num_mostres_class+1
        previous_line=lines
print('El número de muestras clasificadas del fichero' +str(blastx_file) +' con un E-value menor a 1e-5 son: ' + str(num_mostres_class))

                