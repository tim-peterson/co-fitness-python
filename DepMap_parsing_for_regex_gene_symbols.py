

import pandas as pd
#DepMap = pd.read_csv('DepMap_18Q4_gene_effect.csv')
DepMap = pd.read_csv('/Users/timrpeterson/gene_effect_corrected_t.csv')

DepMap.rename(columns=lambda x: x.split()[0], inplace=True)

DepMap.to_csv('/Users/timrpeterson/DepMap_19q1_clean_gene_names.csv')