import csv

with open ('blastx_best_hit.csv','r') as blastx_scnd_filt:
    with open('blastx_best_hit_noblank.csv','w') as out_file:
        writer=csv.writer(out_file)
        for row in csv.reader(blastx_scnd_filt):
            if any(row):
                writer.writerow(row)