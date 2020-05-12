import csv

greater_than = 0.9

base_path = '/Users/timrpeterson/OneDrive-v2/Data/omniphenotype/'



with open(base_path + 'all_KOMP_pearsons_pairwise.complete.obs.csv', mode='r') as csv_file:
#with open('~/Downloads/IMPC_ALL_statistical_results.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    with open(base_path + 'all_KOMP_pearsons_pairwise.complete.obs_gt_' + str(greater_than) + '.csv', 'w') as writefile:

        spamwriter = csv.writer(writefile, delimiter=',')

        #csv_reader = csv.DictReader(csv_file)
        line_count = 0

        for row in csv_reader:

            if line_count > 1:
               # print(row)
                if row[2] != 'NA' and float(row[2]) > greater_than and float(row[2]) < 1:
                    spamwriter.writerow(row)

            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            line_count += 1

        #csv_reader.close()
        #writefile.close()

        #print(f'\t{row["marker_symbol"]} - {row["effect_size"]} effect_size, and {row["p_value"]}.')

