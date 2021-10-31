
import os
import sys
import pandas as pd
import numpy as np
import csv
from collections import Counter
import matplotlib.pyplot as plt

vpf_folder = "/Users/lauratriginer/vpf_tools_laura/test-classified"
db_folder = "/Users/lauratriginer/vpf_tools_laura"

#llegeix classificats i calcula nº de mostres diferents classificades, calcula % també
os.chdir(db_folder) 
num_samples=0
#os.rename(r'AV_subsampled_5kb_contigs.fa',r'AV_subsampled_5kb_contigs.csv') 
with open ('AV_subsampled_5kb_contigs.csv','r') as contigs_file:
    contigs_subset = csv.reader(contigs_file)
    for row in contigs_subset:
        for sample in row:
            if 'MV_' in sample:
                num_samples +=1
    print(num_samples)

os.chdir(vpf_folder)
#with open ('baltimore.tsv', 'r') as balt_class:
  # balt_file = pd.read_csv(balt_class, sep='\\t', engine ='python')
  # class_balt = pd.DataFrame.drop_duplicates(balt_file, subset='virus_name', keep='first').shape[0]
  # print('Porcentaje de muestras clasificadas por Baltimore: ' + str(class_balt/num_samples*100)+ '%')
  # print(class_balt)

with open ('family.tsv', 'r') as fam_class:
  test = pd.read_csv(fam_class, sep='\\t', engine ='python')
  fam_class = pd.DataFrame.drop_duplicates(test, subset='virus_name', keep='first').shape[0]
print('Porcentaje de muestras clasificadas por família: ' + str(fam_class/num_samples*100)+'%')
fam_class_list = pd.DataFrame.drop_duplicates(test,subset='class_name', keep='first')
fam_class_list_num = fam_class_list.shape[0]
#print(fam_class_list['class_name'])
print('Hay ' +str(fam_class_list_num) + ' diferentes familias de virus en la muestra')

    #### SEPARAR LAS MUESTRAS SEGÚN EL MEMBERSHIP RATIO, 4 CUARTILES 99%, 75%, 50%, 25%.
    ## Membership ratio >=99, coger sólo la familia de >99

#fam_mr99 = test.query('membership_ratio > 0.99')
#counts_f99 = fam_mr99['class_name']
#s_99 = Counter(counts_f99)
#print(' Con un membership ratio > 0,99, hay ' + str(s_99))

#labels, values = zip(*s_99.items())
#indexes = np.arange(len(labels))
#width = 1

#plt.bar(indexes, values, width)
#plt.xticks (indexes+ width * 0.5, labels)
#plt.show()

fam_20 = test.query('membership_ratio > 0.99')
#fam_20 = fam_20.query('confidence_score >0.2')
counts_f20 = fam_20['class_name']
s_20 = Counter(counts_f20)
print(' Con un membership ratio > 0,75, hay ' + str(s_20) + 'total= ' + str(sum(s_20.values())))


#fam_mr50 = test.query('membership_ratio > 0.50')
#counts_f50 = fam_mr50['class_name']
#s_50 = Counter(counts_f50)
#print(' Con un membership ratio > 0,50, hay ' + str(s_50))


#fam_mr25 = test.query('membership_ratio > 0.25')
#counts_f25 = fam_mr25['class_name']
#s_25 = Counter(counts_f25)
#print(' Con un membership ratio > 0,25, hay ' + str(s_25))



