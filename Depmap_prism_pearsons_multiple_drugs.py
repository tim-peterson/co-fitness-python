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


#path = "/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/"

path = "/Users/timpeterson/OneDrive-v3/Data/DepMap/"


input_drugs = ["palbociclib"] # "CASP11", 
#input_drugs = ["oxaliplatin"]

output_file_name = "palbociclib_vs_other_drugs"


BROAD_drugs = {}

input_drugs_coded = []
dataset = "primary-screen-replicate-collapsed-treatment-info.csv"
dataset = "secondary-screen-replicate-collapsed-treatment-info.csv"
with open(path + dataset) as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter=",")
	for row in csv_reader:

		if row['name'] == input_drugs[0]:

			input_drugs_coded.append(row['column_name'])
		BROAD_drugs[row['column_name']] = row



drugs = {}
cell_line_d = []
dataset = "primary_screen_replicate_collapsed_logfold_change_t.csv"
dataset = "secondary_screen_replicate_collapsed_logfold_change_t.csv"

with open(path + dataset) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	#next(csv_reader)
	cnt = 0
	for row in csv_reader:
		drug = row[0]
		row.pop(0)
		if cnt == 0:
			cell_line_d = row
			cnt +=1
		else:
			drugs[drug] = row
		

# , path + 'DepMap/02a_BayesianFactors.csv'

output = {}

#shortening the input list for testing purposes
input_drugs_coded = input_drugs_coded[:1]

for x in input_drugs_coded:

	# Build list of NA inside target drug
	target_NAs = [i for i, a in enumerate(drugs[x]) if a == "NA" or a == '']

	for key, value in drugs.items(): 
		'''x, y = np.array(value), np.array(drugs[input[0]])
		nas = np.logical_or(pd.isnull(x), pd.isnull(y))
		result = pearsonr(x[~nas], y[~nas])'''
		dest_NAs = [i for i, a in enumerate(value) if a == "NA" or a == '']

		indices_to_remove = list(set(target_NAs + dest_NAs))

		filtered_value = [i for j, i in enumerate(value) if j not in indices_to_remove] 
		filtered_drug = [i for j, i in enumerate(drugs[x]) if j not in indices_to_remove]
		#all_targets = target_NAs + dest_NAs

		if len(filtered_value) < 2 or len(filtered_drug) < 2:
			continue
		#print(filtered_drug)
		#print(filtered_value)
		result = pearsonr([float(elt) for elt in filtered_value], [float(elt) for elt in filtered_drug])


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

	#if len(value["pearsons"])!=len(input_drugs)*len(datasets): 
	#	continue

	p_adjust = stats.p_adjust(FloatVector(value["pval"]), method = 'BH')
	pval = scipy.stats.stats.combine_pvalues(p_adjust)
	#pval = np.prod(value["pval"])/len(value["pval"])
	result = (sum(value["pearsons"])/len(value["pearsons"]), pval[1])

	output2.append(list((key,) + result)) 

#sort the output desc
output3 = sorted(output2, key=lambda x: x[1], reverse=True)


with open(path + 'interaction_correlations_basal/' + output_file_name + '-pearsons-python-drugs.csv', 'w') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',')

	for row in output3:
		#if any(field.strip() for field in row):

		row.insert(0, BROAD_drugs[row[0]]['name'])
		#if BROAD_drugs[row[0]] == row[0]:

		spamwriter.writerow(row)

	csvfile.close()

