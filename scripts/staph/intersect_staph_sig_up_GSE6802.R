library(tidyverse)

staph1<- read_csv("staph_sig_up_GSE6802.csv")
staph1<- data_frame(genes1=staph1$genes_up)
staph2<- read_csv("staph_gene_list_GSE6802.csv")
staph2<- data_frame(genes2=staph2$Gene.symbol)
staph<-intersect(staph2$genes2, staph1$genes1)%>% as_data_frame()
write.table(staph, file="GSE6802_intersect_staph_sig_up.csv", row.names=F, sep="\t")