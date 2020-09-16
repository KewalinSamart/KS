# Extract data for a given combination of drug and cell-line
# split sig_id and add 4 more columns to the 'vorinostat_ds_annotated@cdesc'

############################################################################################################################

install.packages("devtools")    # to install cmapR from this GitHub repo
## Installing cmapR
devtools::install_github("cmap/cmapR", dependencies=TRUE, force=TRUE) # works

############################################################################################################################
library(cmapR)
library(readr)
library(tidyverse)
library(dplyr)

# Parsing the whole GCTX file
# create a variable to store the path to the level 5 GCTX file

download.file(url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5FLevel5%5FCOMPZ%5Fn118050x12328%5F2017%2D03%2D06%2Egctx%2Egz",
              "Desktop", method="curl")
ds_path <- "GSE70138_Broad_LINCS_Level5_COMPZ_n118050x12328_2017-03-06.gctx"
my_ds <- parse_gctx(ds_path, matrix_only = TRUE)           # don't have enough local memory to hold this

# Parsing a subset of a GCTX file
download.file(url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fsig%5Fmetrics%5F2017%2D03%2D06%2Etxt%2Egz",
              "Desktop", method="curl")
col_meta_path <- "GSE70138_Broad_LINCS_sig_metrics_2017-03-06.txt"
col_meta <- read_delim(col_meta_path, delim = '\t')


# figure out which signatures correspond to vorinostat by searching the 'pert_iname' column
idx <- which(col_meta$pert_iname=="vorinostat")

# and get the corresponding sig_ids
sig_ids <- col_meta$sig_id[idx]

# read only those columns from the GCTX file by using the 'cid' parameter
vorinostat_ds <- parse_gctx(ds_path, cid=sig_ids)


# Adding annotations to a GCT object
# apply the col_meta data.frame as the column anntations to vorinostat_ds
# note that col_meta must have a colum that corresponds to the 'cid' slot of my_ds, aka the 'keyfield'
# note also how the 'cdesc' slot changes after annotating
vorinostat_ds_annotated <- annotate_gct(vorinostat_ds, col_meta, dim="column", keyfield="sig_id")
vorinostat_table_colname <- vorinostat_ds_annotated@cdesc

for (i in 1:nrow(vorinostat_table_colname)) {

  # split the sig_id column into pieces
  sig_id_before_splitting <- as.character(vorinostat_table_colname$sig_id[i])
  sig_id_after_splitting <- strsplit(sig_id_before_splitting, "_")[[1]]
  treatment <- sig_id_after_splitting[1]
  cell_line <- sig_id_after_splitting[2]
  third_before_splitting <- sig_id_after_splitting[3]
  third_after_splitting <- strsplit(third_before_splitting, ":")[[1]]
  time_course <- third_after_splitting[1]
  unknown <- third_after_splitting[2]

  # add four more columns to the original 'vorinostat_ds_annotated@cdesc'
  vorinostat_ds_annotated@cdesc$treatments[i] <- treatment
  vorinostat_ds_annotated@cdesc$cell_lines[i] <- cell_line
  vorinostat_ds_annotated@cdesc$time_courses[i] <- time_course
  vorinostat_ds_annotated@cdesc$unknowns[i] <- unknown
}
