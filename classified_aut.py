## script that calcullates the number of VPF-Class classified samples


import os
import sys
from tkinter.constants import LEFT, RIGHT
import pandas as pd
import numpy as np
import csv
import tkinter as tk
from tkinter import filedialog
from collections import Counter


#VPF-Class's output

vpf_folder = "/Users/lauratriginer/vpf-tools/test-classified"
db_folder = "/Users/lauratriginer/vpf-tools"

os.chdir(db_folder) 
num_samples=0
root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()

#counts number of samples of VPF-Class input.


with open ('AV_subsampled_5kb_contigs.csv','r') as contigs_file:
    contigs_subset = csv.reader(contigs_file)
    for row in contigs_subset:
        for sample in row:
            if 'MV_' in sample:
                num_samples +=1
os.chdir(vpf_folder)

with open (file, 'r') as classf:
  test = pd.read_csv (classf, sep='\\t', engine ='python')
  host_class = pd.DataFrame.drop_duplicates(test, subset='virus_name', keep='first').shape[0]
print(' sample classified % : ' + str(host_class/num_samples*100)+'%')

test2 = pd.DataFrame.drop_duplicates(test,subset='virus_name', keep='first')

#choose a membership ratio. 
class_mr= test2.query('membership_ratio > 0.9')
counts_mr = class_mr['class_name']
cont_mr= Counter(counts_mr)
print(' Given a membership ratio > 0,9 , there are ' + str(cont_mr))


