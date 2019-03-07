

#from pydoc import help
from scipy.stats.stats import pearsonr
#help(pearsonr)

import csv

import numpy as np
 

input = ["ATRAID"]

with open('/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/Third Party/MORPHEOME/Hart-Moffat/qbf_Avanadata_2018.txt') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter='\t')
	next(csv_reader)

	with open('/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/Third Party/MORPHEOME/' + input[0] + 'pearsons-python.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	
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

		sorted(output, key=lambda x: x[1], reverse=True)

		for row in output:		
			spamwriter.writerow(row)


