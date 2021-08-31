
import os
import sys
from tkinter.constants import LEFT, RIGHT, S
import pandas as pd
import numpy as np
import csv
import tkinter as tk
from tkinter import filedialog
from collections import Counter


vpf_folder = "/Users/lauratriginer/vpf-tools/test-classified"
db_folder = "/Users/lauratriginer/vpf-tools"

#llegeix classificats i calcula nº de mostres diferents classificades, calcula % també
os.chdir(db_folder) 
num_samples=0
#os.rename(r'AV_subsampled_5kb_contigs.fa',r'AV_subsampled_5kb_contigs.csv') 
root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()

with open ('AV_subsampled_5kb_contigs.csv','r') as contigs_file:
    contigs_subset = csv.reader(contigs_file)
    for row in contigs_subset:
        for sample in row:
            if 'MV_' in sample:
                num_samples +=1
    print(num_samples)

os.chdir(vpf_folder)

with open (file, 'r') as classf:
  test = pd.read_csv (classf, sep='\\t', engine ='python')
  test=pd.DataFrame.drop_duplicates(test, subset='virus_name', keep='first')
  sampl_class = pd.DataFrame.drop_duplicates(test, subset='virus_name', keep='first').shape[0]
print('Porcentaje de muestras clasificadas: ' + str(sampl_class/num_samples*100)+'%')

class_mr99 = test.query('membership_ratio > 0.99')
counts_f99 = class_mr99['class_name']
s_99 = Counter(counts_f99)
sum_99=sum((s_99).values())
print(sum_99)
print(' Con un membership ratio > 0,99, se han clasificado ' + str(sum_99) +' muestras, de la siguiente manera ' + str(s_99))

class_mr75 = test.query('membership_ratio > 0.75')
counts_f75 = class_mr75['class_name']
s_75 = Counter(counts_f75)
sum_75 = sum((s_75).values())
print(' Con un membership ratio > 0,75, se han clasificado ' + str(sum_75) +' muestras, de la siguiente manera ' + str(s_75))

class_mr50 = test.query('membership_ratio > 0.50')
counts_f50 = class_mr50['class_name']
s_50 = Counter(counts_f50)
sum_s50 = sum((s_50).values())
print(' Con un membership ratio > 0,50, se han clasificado ' + str(sum_s50) +' muestras, de la siguiente manera ' + str(s_50))


class_mr25 = test.query('membership_ratio > 0.25')
counts_f25 = class_mr25['class_name']
s_25 = Counter(counts_f25)
sum_s25 = sum((s_25).values())
print(' Con un membership ratio > 0,25, se han clasificado ' + str(sum_s25) +' muestras, de la siguiente manera ' + str(s_25))
