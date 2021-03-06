#from pydoc import help
import scipy
from scipy.stats.stats import pearsonr

from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import FloatVector

stats = importr('stats')



import csv
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


path = "/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/"

input_genes = ["TGFBR2", "TGFBR1", "SMAD3", "FBN1"]
input_genes = ["CHUK","MAP3K14","NFKB1","NFKB2","NFKBIA","REL","RELA","RELB","RPS3"]
input_genes = ["BMP4","BMP8A","BMP8B","CLEC11A","FGF13","FGF14","GDF7","IGF2","MDK","OGN","PDGFD","TGFB2","TGFB3","THBS4"]
input_genes = ["ADAMTS15","AGER","APLP1","BMP2","BMP4","BMP8A","BMP8B","CCDC80","CCL12","CCL17","CCL2","CCL22","CCL5","CCL7","CCL8","CCL9","CHRD","CLEC11A","COL13A1","COL5A1","COL5A3","CX3CL1","CXCL10","CXCL13","CXCL14","CXCL16","CXCL9","FBN1","FGF13","FGF14","FGF23","FN1","FSTL1","GAL","GDF7","IGF2","INHBA","INSL3","LAMC2","LIF","LIPC","LTB","LTBP2","MDK","NDNF","NELL1","NGF","NOV","NPY","OGN","PCOLCE","PCOLCE2","PDGFB","PDGFD","PLA2G2D","POSTN","PTN","PTPRS","RSPO3","RTN4R","SAA3","SMOC2","SPP1","TGFB2","TGFB3","THBS2","THBS3","THBS4","TIMP1","TNFSF11","TNFSF8","WNT1","WNT10A","WNT7B"]
input_genes = ['CHUK','MAP3K14','NFKB1','NFKB2','NFKBIA','REL','RELA','RELB','RPS3','BMP4','BMP8A','BMP8B','CLEC11A','FGF13','FGF14','GDF7','IGF2','MDK','OGN','PDGFD','TGFB2','TGFB3','THBS4']
input_genes = ['SLC37A3', 'ATRAID', 'FDPS']
input_genes = ['MTOR']
input_genes = ['TGFBR1']
input_genes = ['EIF4G2', 'PRRC2A', 'PRR2C']


output_file_name = "SLC37A3_ATRAID_FDPS_depmap_tcga_gtex"
output_file_name = "MTOR_gtex_xena_TCGA_normal"
output_file_name = "TGFBR1_gtex_xena_TCGA_normal"
output_file_name = "EIF4G2_depmap"

datasets = [path + 'DepMap/gene_effect_corrected_output.csv',
 path + 'Hart-Moffat/qbf_Avanadata_2018.txt',
 #path + 'GEPIA/GEPIA_TCGA_normal.csv',
 #path + 'xena/xena_tcga_all_normal_gtex_genes_only.csv',
 #path + 'GTEX/gtex_get_depmap_genes.csv',
 ]

output = {}
for x in input_genes:

	for y in datasets:

		print(y)

		if "gene_effect" in y:
			delimiter = ','
			remove_gene_id = True
		elif "qbf_Avanadata" in y:
			delimiter = '\t'
			remove_gene_id = False 			
		else:
			delimiter = ','
			remove_gene_id = False 

		with open(y) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=delimiter)
			next(csv_reader)

			genes = {}
			for row in csv_reader:

				if "gtex" in y:
					gene = row[1]
					row.pop(0)
					row.pop(0)
				else:
					gene = row[0]
					row.pop(0)

				if remove_gene_id is True:
					arr = gene.split()
				#row_temp.pop(0)
					genes[arr[0]] = row
				else:
					genes[gene] = row

			for key, value in genes.items(): 

				if x not in genes:

					continue

				if sum(value) !=0:

					result = pearsonr(np.array(value).astype(np.float), np.array(genes[x]).astype(np.float))

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
	if "pval" in value:
		p_adjust = stats.p_adjust(FloatVector(value["pval"]), method = 'BH')
		pval = scipy.stats.stats.combine_pvalues(p_adjust)
		pval1 = pval[1]
	else:
		pval1 = 0	
	#pval = np.prod(value["pval"])/len(value["pval"])
	result = (sum(value["pearsons"])/len(value["pearsons"]), pval1)

	output2.append(list((key,) + result)) 

#sort the output desc
output3 = sorted(output2, key=lambda x: x[1], reverse=True)


with open(path + 'interaction_correlations_basal/' + output_file_name + '-pearsons-python.csv', 'w') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',')

	for row in output3:
		#if any(field.strip() for field in row):
		spamwriter.writerow(row)

	csvfile.close()

