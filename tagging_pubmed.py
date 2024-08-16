import pandas as pd
from Bio import Entrez
import time

def read_gene_names_from_excel(file_path):
    """Read and return the list of gene names from an Excel file."""
    data = pd.read_excel(file_path)
    return data['Gene'].unique().tolist()

def search_pubmed(gene_name):
    """Search PubMed for articles related to a specific gene and tag sites."""
    Entrez.email = "s2552113@ed.ac.uk"  # Replace with your email
    query = f"{gene_name} AND tag site"
    handle = Entrez.esearch(db="pubmed", term=query, retmax=50)
    record = Entrez.read(handle)
    handle.close()
    return record['IdList']

def save_results_to_excel(gene_pubmed_ids, output_file):
    """Save the PubMed ID results to an Excel file."""
    # Convert dictionary to DataFrame
    df = pd.DataFrame(list(gene_pubmed_ids.items()), columns=['Gene', 'PubMed IDs'])
    # Save DataFrame to Excel
    df.to_excel(output_file, index=False)

# Path to the Excel file
file_path = 'C:/Users/Lenovo/Desktop/dissertation/dataset/Gene_level_Cterminus.xlsx'

# Output Excel file path
output_file = 'C:/Users/Lenovo/Desktop/dissertation/dataset/PubMed_IDs_output_Cterminus.xlsx'

# Read gene names from the Excel file
gene_names = read_gene_names_from_excel(file_path)

# Dictionary to hold gene names and their corresponding PubMed IDs
gene_pubmed_ids = {}

# Perform PubMed searches
for gene in gene_names:
    pubmed_ids = search_pubmed(gene)
    gene_pubmed_ids[gene] = pubmed_ids
    print(f"Gene: {gene}, PubMed IDs: {pubmed_ids}")
    time.sleep(1)  # Pause to prevent overwhelming the server

# Save results to Excel
save_results_to_excel(gene_pubmed_ids, output_file)

print(f"Results have been saved to {output_file}.")
