

geneA = "FDPS"

dataset = "depmap"

path = "/Users/timrpeterson/OneDrive - Washington University in St. Louis/Data/MORPHEOME"

#geneA = "PQLC3"
if dataset == 'depmap_2018q4':
    files = [path."/Hart-Moffat/qbf_Avanadata_2018.csv"]
elseif dataset == 'depmap_2019q1':
    files = [path."/DepMap/gene_effect_corrected_output.csv"]
elseif dataset == 'sanger':
    files = [path."/DepMap/02a_BayesianFactors.csv"]
elseif dataset == 'shrna':
    files = [path."/Hart-Moffat/134346-1-shRNA-bayesian-factors.csv"]
elseif dataset == 'depmap':
    files = [path."/Hart-Moffat/qbf_Avanadata_2018.csv", path."/DepMap/gene_effect_corrected_output.csv"]
elseif dataset == 'depmap_broad_sanger':
    files = [path."/Hart-Moffat/qbf_Avanadata_2018.csv", path."/DepMap/gene_effect_corrected_output.csv",
path."/DepMap/02a_BayesianFactors.csv"]
elseif dataset == 'tcga':
    files = [path."/xena/xena_tcga_all_normal_gtex_genes_only.csv"]
elseif dataset == 'gtex':
    files = [path."/GTEX/gtex_get_depmap_genes.csv"]
elseif dataset == 'gtex_tcga':
    files = [path."/GTEX/gtex_get_depmap_genes.csv", path."/xena/xena_tcga_all_normal_gtex_genes_only.csv"]
elseif dataset == 'all':
    files = [path."/Hart-Moffat/qbf_Avanadata_2018.csv", 
    path."/DepMap/gene_effect_corrected_output.csv", 
    path."/DepMap/02a_BayesianFactors.csv",
    path."/GTEX/gtex_get_depmap_genes.csv", 
    path."/xena/xena_tcga_all_normal_gtex_genes_only.csv"]
else:
    dd('no dataset')

new_arr = []


for gene in geneA :
    #dd(gene)
    for file in files :
        #print_r(file)
         #output_dir.
        if file, "r") ) !== FALSE:

            row = 1
            genes = []
            /*if file, "qbf")!==false:
                delimiter = "\t"
            else delimiter = ","*/
            delimiter = ","

            while ((line = fgetcsv(handle,  0, delimiter )) !== FALSE){

                if file, "GTEX")!==false:

                    line0 = line
                    array_shift(line0)
                    array_shift(line0)

                    genes[line[1]] = line0

                else{
                    if(row == 1){ 
                        row++ 
                        continue 

                    line0 = line
                    array_shift(line0)

                    if file, "gene_effect_corrected_output")!==false:
                        gene_arr = explode(" ", line[0])
                        genes[gene_arr[0]] = line0
                    else genes[line[0]] = line0
                #dd(genes)

            for key => val in genes :

                if(array_sum(val)==0) continue

                if new_arr[key]):
                    #dd(key)
                    new_arr[key] = [pearson_correlation( genes[gene] , val )]
                else{
                    new_arr[key][] = pearson_correlation( genes[gene] , val )
                
            #foreach(line)
            
        fclose(handle)            


# dd(array_slice(new_arr, 0, 5))

new_arr0 = []
for key => val in new_arr :

    if( count(val)!=count(files)*count(geneA) ) continue

    #array = array_filter(val, function(a) { return (a !== 0) })
    new_arr0[]= [key, array_sum(val)/count(val)]

usort(new_arr0, function(a, b) {
    return a[1] <=> b[1]

new_arr0 = array_reverse(new_arr0)


arr = []

for gene in geneA :

    if path."/NickJacobs/gene_gene_paper_count_greater_than_0.csv", "r") ) !== FALSE:

        while ((line = fgetcsv(handle,  0, ",")) !== FALSE){

            if line[0]==gene:
                if arr[line[1]]):
                     arr[line[1]] = line[2]
                else{
                    arr[line[1]] = arr[line[1]] + line[2]
               

            if line[1]==gene:
                #arr[line[0]] = line[2]

                if arr[line[0]]):
                     arr[line[0]] = line[2]
                else{
                    arr[line[0]] = arr[line[0]] + line[2]

        
    fclose(handle)


query = 'SELECT * from `morpheome`.genes'

#dd(query)
hits = DB.select(query)

descriptions = []

for hit in hits :
        descriptions[hit->Symbol] = hit->Full_name_from_nomenclature_authority


if "_", geneA)."-".dataset."-geneX-pearsons_with_papers.csv", "w") ) !== FALSE:

    fputcsv(handle1, ['gene', 'pearsons', 'papers with '.implode("_", geneA), 'gene_description'] )


    for arr0 in new_arr0 :

        if arr[arr0[0]]):
            #arr[] = [line[0], line[1]]
            temp = array_merge(arr0, [arr[arr0[0]]] )
        else{
            temp = array_merge(arr0, [0])

        if descriptions[arr0[0]]):
            fputcsv(handle1, array_merge(temp, [descriptions[arr0[0]] ]  ) )
        else{
            fputcsv(handle1, array_merge(temp, ["no description"]) )

        #fputcsv(handle1, arr)
    
fclose(handle1)


