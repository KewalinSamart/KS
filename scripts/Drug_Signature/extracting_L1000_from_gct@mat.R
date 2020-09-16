if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

library(readr)
library(tidyverse)
library(dplyr)

BiocManager::install("AnnotationDbi")
library(AnnotationDbi)

# org.Hs.eg.db works!
# url: https://davetang.org/muse/2013/12/16/bioconductor-annotation-packages/
BiocManager::install("org.Hs.eg.db")
library(org.Hs.eg.db)

# gene symbol to entrez id 
my_genes <- c("ANXA7")

#symbol and OMIM
a <- select(org.Hs.eg.db,
            keys = my_genes,
            columns=c("ENTREZID", "SYMBOL"),
            keytype="SYMBOL")

gene_ent_id <- as.character(a[2:2])

# entrez id to gene symbol
my_genes <- c("780")

#symbol and OMIM
a <- select(org.Hs.eg.db,
            keys = my_genes,
            columns=c("ENTREZID", "SYMBOL"),
            keytype="ENTREZID")

gene_symbol <- as.character(a[2:2])


BiocManager::install("HGNChelper")
library(HGNChelper)
#url: https://cran.r-project.org/web/packages/HGNChelper/HGNChelper.pdf

# checking on the 'checkGeneSymbols' fuction's return format
gene_validity_table <- checkGeneSymbols("ERO1L", unmapped.as.na = TRUE, map = NULL,
                                        species = "human")
gene_validity_table[1,2] # bool type

#get L1000 gene list (obtained from http://amp.pharm.mssm.edu/l1000fwd/download_page)
L1000<- read_csv("Probes_L1000_metadata.csv")
gene_names_L1000 <- data.frame(pr_gene_symbol = L1000$pr_gene_symbol)  

# This for-loop replace each row of L1000_ent_id with their corresponding entrez gene ids
for (i in 1:nrow(gene_names_L1000)) {
  my_gene <- c(as.character(gene_names_L1000$pr_gene_symbol[i]))
  gene_validity_table <- checkGeneSymbols(my_gene, unmapped.as.na = TRUE, map = NULL,
                                          species = "human")
  if (gene_validity_table[1,2] == TRUE ){
    a <- select(org.Hs.eg.db,
                keys = my_gene,
                columns=c("ENTREZID", "SYMBOL"),
                keytype="SYMBOL")
    gene_ent_id <- as.character(a[2:2])
    gene_names_L1000$L1000_ent_id[i] <- gene_ent_id 
  }
  if (gene_validity_table[1,2] == FALSE) {
    gene_ent_id = 'NA'
    gene_names_L1000$L1000_ent_id[i] <- gene_ent_id
  } 
}

# view the changes made to the 'gene_names_L1000' dataframe
View(gene_names_L1000)

# output 'gene_names_L1000' as a csv file and import it for further analyses
write.csv(gene_names_L1000, file="gsymbols_entrezid_L1000.csv", row.names=F)
gene_names_L1000 <- read_csv("gsymbols_entrezid_L1000.csv")

### intersect 'gene_names_L1000$L1000_ent_id' with 'vorinostat_ds@rid' ###
gene_names_L1000$L1000_ent_id
View(gene_names_L1000$L1000_ent_id)

# store the rows of the GCT object 'vorinostat_ds' in 'vorinostat_ds_entrez_id' 
vorinostat_ds_entrez_id <- vorinostat_ds@rid

# create a new dataframe containing overlapping genes in the landmark genes and the 'vorinostat_ds_entrez_id'
intersect_L1000_vorinostat <- intersect(gene_names_L1000$L1000_ent_id, vorinostat_ds_entrez_id)%>% as_tibble()

# create a list to store the overlapping genes
intersect_L1000_vorinostat_list <- list()
for (i in 1:936){
  n <- intersect_L1000_vorinostat$value[i]
  intersect_L1000_vorinostat_list <- append(intersect_L1000_vorinostat_list, n)
}

# extract only landmark genes from 'vorinostat_matrix'
vorinostat_matrix <- vorinostat_ds@mat 
vorinostat_matrix <- subset(vorinostat_matrix, rownames(vorinostat_matrix) %in% intersect_L1000_vorinostat_list)

write.csv(vorinostat_matrix, file = "vorinostat_matrix.csv", quote=FALSE)
