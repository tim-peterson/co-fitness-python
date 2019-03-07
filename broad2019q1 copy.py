

#from pydoc import help
from scipy.stats.stats import pearsonr
#help(pearsonr)

import csv

import numpy as np
 

#https://stackoverflow.com/questions/4869189/how-to-transpose-a-dataset-in-a-csv-file
'''from itertools import izip
a = izip(*csv.reader(open("/Users/timrpeterson/Downloads/gene_effect_corrected.csv", "rb")))
csv.writer(open("/Users/timrpeterson/Downloads/gene_effect_corrected_output.csv", "wb")).writerows(a)
quit()'''
input = ["ATRAID (51374)"]
input = ["MTOR (2475)"]
input = ["SLC37A3 (84255)"]
input = ["FDPS (2224)"]

'''with open('/Users/timrpeterson/Downloads/gene_effect_corrected_output.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	next(csv_reader)

quit()	'''
with open('/Users/timrpeterson/Downloads/gene_effect_corrected_output.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	next(csv_reader)

	with open('/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/Third Party/MORPHEOME/' + input[0] + '-pearsons-python-q1.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
	
		genes = {}
		for row in csv_reader:
			gene = row[0]
			row.pop(0)

			#row_temp.pop(0)
			genes[gene] = row

		#for k, v in genes.iteritems():
			#print k, v
			#quit()
		output = []
		for key, value in genes.iteritems(): 

			result = pearsonr(np.array(value).astype(np.float), np.array(genes[input[0]]).astype(np.float))

			output.append(list((key,) + result)) 

		output2 = sorted(output, key=lambda x: x[1], reverse=True)

		for row in output2:		
			#if any(field.strip() for field in row):
			spamwriter.writerow(row)

		csvfile.close()

