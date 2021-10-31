# TFM ANÁLISIS COMPUTACIONAL DE METAVIROMAS EN AMBIENTES HIPERSALINOS

Scripts programados para la clasificación y análisis de muestras del TFM.

blastx_add_fam_and_gen.py 
Añade la família y el género de una base de datos al archivo ya clasificado.

blastx_count_samples_classified_evalue.py
Cuenta el número de muestras clasificadas por BlastX dado un valor máximo de e-value.

exec1.py
Se introduce un membership ratio elegido y se seleccionan dos archivos. Se obtiene la clasificación de las muestras dado el membership ratio introducido

vpf_count_sample_classified.py
script que calcula el número de muestras clasificadas por VPF-Class

tsv_vpf_classification.py

Concatena los archivos .tsv, elimina las muestras que pudiera haber duplicadas, cuenta el número de muestras clasificadas y cómo está distribuida la clasificación.
