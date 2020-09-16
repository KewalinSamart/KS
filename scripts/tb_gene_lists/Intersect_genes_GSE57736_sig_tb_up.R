library(tidyverse)

tb1<- read_csv("tb_up_sig_GSE57736 .csv")
tb1<- data_frame(genes1=tb1$genes_up)
tb2<- read_csv("GSE57736_gene_list.csv")
tb2<- data_frame(genes2=tb2$GENE_SYMBOL)
tb<-intersect(tb2$genes2, tb1$genes1)%>% as_data_frame()
write.table(tb, file="GSE57736_intersect_tb_up_sig_GSE57736.csv", row.names=F, sep="\t")