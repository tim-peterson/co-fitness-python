

#from pydoc import help
from scipy.stats.stats import pearsonr
#help(pearsonr)

import csv

import numpy as np
 

'''import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="morpheome")        # name of the data base
'''
# you must create a Cursor object. It will let
#  you execute all the queries you need
'''cur = db.cursor()

gene_list = []
# Use all the SQL you like
cur.execute("SELECT name FROM aliases")

# print all the first cell of all the rows
for row in cur.fetchall():
    #print row[0]
    gene_list.append(row[0])

db.close()

print(gene_list)
quit()'''

#https://stackoverflow.com/questions/4869189/how-to-transpose-a-dataset-in-a-csv-file
'''from itertools import izip
a = izip(*csv.reader(open("/Users/timrpeterson/Downloads/gene_effect_corrected.csv", "rb")))
csv.writer(open("/Users/timrpeterson/Downloads/gene_effect_corrected_output.csv", "wb")).writerows(a)
quit()'''
input = ["ATRAID (51374)"]

input = ["SLC37A3 (84255)"]
input = ["FDPS (2224)"]
input = ["MTOR (2475)"]
input = ["TGFBR2 (7048)"]
input = ["TGFBR1 (7046)"]
input = ["FBN1"]
input = ["SMAD3"]
input = ["TGFBR2"]
'''with open('/Users/timrpeterson/Downloads/gene_effect_corrected_output.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	next(csv_reader)

quit()	'''

dataset = '/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/DepMap/gene_effect_corrected_output.csv'
dataset = '/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/Hart-Moffat/qbf_Avanadata_2018.txt'

if "gene_effect" not in dataset:
	age = '2018q4'
	delimiter = '\t'
	remove_gene_id = False 
else:
	age = '2019q1'
	delimiter = ','
	remove_gene_id = True 

with open(dataset) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=delimiter)
	next(csv_reader)

	with open('/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME/DepMap/cherry-picked/' + input[0] + '-pearsons-python-' + age + '.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
	
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
		#for k, v in genes.iteritems():
			#print k, v
			#quit()
		output = []
		for key, value in genes.iteritems(): 

			result = pearsonr(np.array(value).astype(np.float), np.array(genes[input[0]]).astype(np.float))

			output.append(list((key,) + result)) 

			#sort the output desc
		output2 = sorted(output, key=lambda x: x[1], reverse=True)

		for row in output2:		
			#if any(field.strip() for field in row):
			spamwriter.writerow(row)

		csvfile.close()

