#!/anaconda3/bin/python3

import pandas as pd

def loadGeneList(gene_list_txt):
    
    gene_list=[]
    
    with open(gene_list_txt) as genes:
        for line in genes:
            lista=line.strip().split()
            gene_list.append((lista[0],lista[1]))
    
    return gene_list

def extract_column(expr_file, col_name="", print_head=False):
    
    table = pd.read_csv(expr_file, sep="\t")
    columns_name = list(table)
    if print_head:
        print(table.head())
    if col_name in columns_name:
        list_req = list(table[col_name])
    else:
        print("The colum name specified is not present in your data")
        list_req=[]
        
    return list_req

def get_gene_list(gencode_gtf):
    gene_list=[]
    i=0
    with open(gencode_gtf) as gtf:
        for line in gtf:
            i+=1
            if not line.startswith("#"):
                lista = line.strip().split("\t")
                if len(lista) >= 9:
                    if lista[2].strip() == "gene":
                        chromosome = lista[0]
                        gene_name = lista[8].split(";")[0].split()[1].split('"')[1]
                            
                        if not (chromosome, gene_name) in gene_list:
                            gene_list.append((chromosome, gene_name))
                        else:
                            pass
                else:
                    pass
    return gene_list



