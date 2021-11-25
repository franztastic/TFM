
import os
import sys
from tkinter.constants import LEFT, RIGHT, S
import pandas as pd
import numpy as np
import csv
import tkinter as tk
from tkinter import filedialog
from collections import Counter

def filt_by_mr (membership_ratio , file_vpf_output, file_fasta):

#llegeix classificats i calcula nº de mostres diferents classificades, calcula % també
    num_samples=0
    os.rename (str(file_fasta), (str(file_fasta) +'.csv'))

    with open (file_fasta,'r') as contigs_file:
        contigs_subset = csv.reader(contigs_file)
        for row in contigs_subset:
            for sample in row:
                if 'MV_' in sample:
                    num_samples +=1

    with open (file_vpf_output, 'r') as classf:
        test = pd.read_csv (classf, sep='\\t', engine ='python')
        test=pd.DataFrame.drop_duplicates(test, subset='virus_name', keep='first')
        sampl_class = pd.DataFrame.drop_duplicates(test, subset='virus_name', keep='first').shape[0]

        class_mr = test.query(str('membership_ratio > '+ membership_ratio))
        counts_fmr = class_mr['class_name']
        s_kr = Counter(counts_fmr)
        sum_mr=sum((s_kr).values())
        return (sum_mr, s_kr)

#step 1. Choose vpf-output-classified.tsv
root = tk.Tk()
root.withdraw()
file_vpf_output = filedialog.askopenfilename()

membership_ratio = int(0.75)
#step 2. Choose the original .fasta file 

root = tk.Tk()
root.withdraw()
file_fasta = filedialog.askopenfilename()


classif, cont = filt_by_mr(membership_ratio, file_vpf_output, file_fasta)

print(' Con un membership ratio > '+membership_ratio + ' se han clasificado ' + classif +' muestras, de la siguiente manera ' + cont)

