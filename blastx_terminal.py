
export PATH=$PATH:$HOME/ncbi-blast-2.11.0+/bin
export BLASTDB=$HOME/blastdb
set BLASTDB=$HOME/blastdb


#if file format is FASTA, must use makeblastdb
#creating NUCLEOTIDE database with short contigs
#makeblastdb -in viral_genomic.fsa -dbtype nucl -parse_seqids -out contigsblast
#creating PROTEIN blast database to compare shortdb with longdb
#makeblastdb -in viral_prot.fsa -dbtype prot -parse_seqids -out viralprotblast

##  BLASTX CONTIG AGAINST DATABASE
#blastx -query viral_genomic.fsa -subject viral_prot.fsa -out resultat1.out -outfmt "6 delim=@ sseq sseqid evalue" -num_alignments 10
blastx -query viral_genomic.fsa -subject viral_prot.fsa -out results.csv 

    #" -query = secuencia de problema 
    #" subject = archivo fasta con la secuencia a la que enfrentaremos nuestra secuencia
    #" out nombre del archivo de salida.

    #return [scores,nuc_seq]
    
