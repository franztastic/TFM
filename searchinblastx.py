#def searchinblastx (newiddb, newseq, bd2comp_id,bd2comp_nuc)

    
    #export PATH=$PATH:$HOME/ncbi-blast-2.11.0+/bin
    #export BLASTDB=$HOME/blastdb
    #set BLASTDB=$HOME/blastdb

import os
import sys
from Bio import SeqIO
import shutil
import os.path

sys.path.append('/HOME/ncbi-blast-2.11.0+/bin/')
sys.path.append('/HOME/blastdb/')
NUCLEOTIDE_DB='/Users/lauratriginer/blastdb/viral.3.1.genomic.fna'
BIG_DB_PROT ='/Users/lauratriginer/blastdb/viral.3.protein.faa'

#COPY DATABASES TO CURRENT PATH
######NUCLEOTIDE
shutil.copy2(NUCLEOTIDE_DB, str(os.getcwd()+'/'))
os.rename(r'viral.3.1.genomic.fna',r'viral_genomic.fsa') 
######PROTEIN
shutil.copy2(BIG_DB_PROT, str(os.getcwd()+'/'))
os.rename(r'viral.3.protein.faa',r'viral_prot.fsa') 

#if file format is FASTA, must use makeblastdb
#creating NUCLEOTIDE database with short contigs
#makeblastdb -in viral_genomic.fsa -dbtype nucl -parse_seqids -out contigsblast
#creating PROTEIN blast database to compare shortdb with longdb
#makeblastdb -in viral_prot.fsa -dbtype prot -parse_seqids -out viralprotblast

##  BLASTX CONTIG AGAINST DATABASE
#blastx -query viral_genomic.fsa -subject viral_prot.fsa -out resultat1.out -outfmt "6 delim=@ sseq sseqid evalue" -num_alignments 10
blastx -query viral_genomic.fsa -subject viral_prot.fsa -out resultats.csv 

    #" -query = secuencia de problema 
    #" subject = archivo fasta con la secuencia a la que enfrentaremos nuestra secuencia
    #" out nombre del archivo de salida.

    #return [scores,nuc_seq]
    
