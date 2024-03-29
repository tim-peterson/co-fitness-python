#from pydoc import help
import scipy
from scipy.stats.stats import pearsonr

from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import FloatVector

stats = importr('stats')

'''p_adjust = stats.p_adjust(FloatVector([0.03,0.01,0.2]), method = 'BH')

print(p_adjust)
quit()'''
#help(pearsonr)

import csv
import sys
import pandas as pd
import numpy as np

input = ["ATRAID (51374)"]
input = ["SLC37A3 (84255)"]
input = ["FDPS (2224)"]
input = ["MTOR (2475)"]
input = ["TGFBR2 (7048)"]
input = ["TGFBR1 (7046)"]
input = ["FBN1"]
input = ["SMAD3"]
input = ["TGFBR2"]
input = ["FDPS (2224)"]

#path = "/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/"

path = "/Users/timpeterson/OneDrive-v3/Data/DepMap/"


input_genes = ["TGFBR2", "TGFBR1", "SMAD3", "FBN1"]
input_genes = ["CHUK","MAP3K14","NFKB1","NFKB2","NFKBIA","REL","RELA","RELB","RPS3"]
input_genes = ["BMP4","BMP8A","BMP8B","CLEC11A","FGF13","FGF14","GDF7","IGF2","MDK","OGN","PDGFD","TGFB2","TGFB3","THBS4"]
input_genes = ["ADAMTS15","AGER","APLP1","BMP2","BMP4","BMP8A","BMP8B","CCDC80","CCL12","CCL17","CCL2","CCL22","CCL5","CCL7","CCL8","CCL9","CHRD","CLEC11A","COL13A1","COL5A1","COL5A3","CX3CL1","CXCL10","CXCL13","CXCL14","CXCL16","CXCL9","FBN1","FGF13","FGF14","FGF23","FN1","FSTL1","GAL","GDF7","IGF2","INHBA","INSL3","LAMC2","LIF","LIPC","LTB","LTBP2","MDK","NDNF","NELL1","NGF","NOV","NPY","OGN","PCOLCE","PCOLCE2","PDGFB","PDGFD","PLA2G2D","POSTN","PTN","PTPRS","RSPO3","RTN4R","SAA3","SMOC2","SPP1","TGFB2","TGFB3","THBS2","THBS3","THBS4","TIMP1","TNFSF11","TNFSF8","WNT1","WNT10A","WNT7B"]
input_genes = ['CHUK','MAP3K14','NFKB1','NFKB2','NFKBIA','REL','RELA','RELB','RPS3','BMP4','BMP8A','BMP8B','CLEC11A','FGF13','FGF14','GDF7','IGF2','MDK','OGN','PDGFD','TGFB2','TGFB3','THBS4']


input_genes = ["MTOR", "RPTOR", "RICTOR", "MLST8"]

output_file_name = "MTOR_RPTOR_genes_v6"

input_genes = ['IRF8','IRF4','IRF9']

input_genes = ["ATRAID..51374.", "SLC37A3..84255."]

input_genes = ["ATRAID", "SLC37A3", 'FDPS']

input_genes = ["CASP1", "NLRP3", "GSDMD", "GSDME"] # "CASP11", 

input_genes = ["PPARA"] # , "LPIN1", "SIRT3"

output_file_name = "PPARA_genes"

#datasets = [path + 'DepMap/gene_effect_corrected_output.csv', path + 'Hart-Moffat/qbf_Avanadata_2018.csv', path + 'DepMap/02a_BayesianFactors.csv']

datasets = [path + 'gene_effect_corrected_t_clean_gene_name.csv', path + 'qbf_Avanadata_2018.csv', path + '02a_BayesianFactors.csv']


datasets = [path + 'gene_effect_corrected_t_clean_gene_name.csv']

datasets = [path + 'Achilles_gene_effect-2019q4-Broad_t_noNAs.csv']

datasets = [path + 'depmap_2020q2_t.csv']
#datasets = [path + 'Hart-Moffat/134346-1-shRNA-bayesian-factors.txt']

'''if "depmap_broad_sanger" in sys.argv[1]:
datasets = [path + 'DepMap/gene_effect_corrected_output.csv', 'Hart-Moffat/qbf_Avanadata_2018.txt']

else
datasets = [path + 'DepMap/gene_effect_corrected_output.csv', 'Hart-Moffat/qbf_Avanadata_2018.txt']
'''
# , path + 'DepMap/02a_BayesianFactors.csv'

output = {}
for x in input_genes:

	for y in datasets:

		delimiter = ','
		if "depmap_2020q2" in y:
			age = '2020q2'
			delimiter = ','
			remove_gene_id = True		
		if "gene_effect" not in y:
			#age = '2018q4'
			#delimiter = '\t'
			remove_gene_id = True #False
		else:
			#age = '2019q1'
			#delimiter = ','
			remove_gene_id = True 

		with open(y) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=delimiter)
			next(csv_reader)

			genes = {}
			for row in csv_reader:
				gene = row[0]
				row.pop(0)

				if remove_gene_id is True:
					arr = gene.split()
				#row_temp.pop(0)
					genes[arr[0]] = row
				else:
					genes[gene] = row



				'''			
				for key, value in genes.items(): 

					if x not in genes:

						continue

					#a, b = pd.isnull(np.array(value, dtype=float)), 
					a, b = value, genes[x]
					#nas = np.logical_or(a.isnan(), b.isnan())
					nas = np.logical_or(pd.isnull(value), pd.isnull(genes[x]))

					#result = pearsonr(a[~nas], b[~nas])
					result = pearsonr(np.array(value).astype(np.float)[~nas], np.array(genes[x]).astype(np.float)[~nas])
					#result = pearsonr(np.array(value).astype(np.float), np.array(genes[x]).astype(np.float))
				'''
					

			# Build list of NA inside target gene
			target_NAs = [i for i, a in enumerate(genes[x]) if a == "NA" or a == '']

			for key, value in genes.items(): 
				'''x, y = np.array(value), np.array(genes[input[0]])
				nas = np.logical_or(pd.isnull(x), pd.isnull(y))
				result = pearsonr(x[~nas], y[~nas])'''
				dest_NAs = [i for i, a in enumerate(value) if a == "NA" or a == '']

				indices_to_remove = list(set(target_NAs + dest_NAs))

				filtered_value = [i for j, i in enumerate(value) if j not in indices_to_remove] 
				filtered_gene = [i for j, i in enumerate(genes[x]) if j not in indices_to_remove]
				#all_targets = target_NAs + dest_NAs

				#print(filtered_gene)
				#print(filtered_value)
				result = pearsonr([float(elt) for elt in filtered_value], [float(elt) for elt in filtered_gene])


				if key in output:

					output[key]["pearsons"].append(result[0])

					if "pval" in output[key] and result[1]!=0:

						output[key]["pval"].append(result[1])

					elif "pval" not in output[key] and result[1]!=0: 

						output[key]["pval"] = [result[1]]
				else:

					if result[1]!=0: 

						output[key] = {"pearsons" : [result[0]],"pval" : [result[1]]}
					else:
						output[key] = {"pearsons" : [result[0]]}
				#output.append(list((key,) + result)) 

				#sort the output desc
			#output2 = sorted(output, key=lambda x: x[1], reverse=True)

output2 = []
for key, value in output.items():

	if len(value["pearsons"])!=len(input_genes)*len(datasets): 
		continue

	p_adjust = stats.p_adjust(FloatVector(value["pval"]), method = 'BH')
	pval = scipy.stats.stats.combine_pvalues(p_adjust)
	#pval = np.prod(value["pval"])/len(value["pval"])
	result = (sum(value["pearsons"])/len(value["pearsons"]), pval[1])

	output2.append(list((key,) + result)) 

#sort the output desc
output3 = sorted(output2, key=lambda x: x[1], reverse=True)


with open(path + 'interaction_correlations_basal/' + output_file_name + '-pearsons-python.csv', 'w') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',')

	for row in output3:
		#if any(field.strip() for field in row):
		spamwriter.writerow(row)

	csvfile.close()

