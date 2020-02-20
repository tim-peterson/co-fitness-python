# Load pickles data
pickles_data <- read.table("/Users/timrpeterson/OneDrive-v2/Data/MORPHEOME/all_crispria_7-26-19.csv",header = TRUE, sep = ",",
                           stringsAsFactors = FALSE)

pickles_data <- read.table("/Users/timrpeterson/OneDrive-v2/Data/MORPHEOME/DepMap/Achilles_gene_effect-2019q4-Broad.csv",header = TRUE, sep = ",",
                           stringsAsFactors = FALSE)

#Column names
#genes_pickles <- pickles_data$GENE
genes_pickles <- pickles_data$gene

# Pairwise Correlation
x <- cor(t(pickles_data[, -1]))
#rownames(x) <- colnames(x) <- pickles_data$GENE
rownames(x) <- colnames(x) <- pickles_data$gene
x <- reshape::melt(t(x))
x <- x[ order(x$X1, x$X2), ]

write.csv(x,"/Users/timrpeterson/OneDrive-v2/Data/MORPHEOME/all_crispria_pearsons.csv",row.names=FALSE,quote=FALSE)
# Optional
#write.csv(x[1:33744481,], "All_17427_Genes_Correlation_Full_1.csv",row.names=FALSE)