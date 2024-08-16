import pandas as pd
import requests


file_path = 'C:/Users/Lenovo/Desktop/dissertation/indel/DMS_indels.csv'
data = pd.read_csv(file_path)

def fetch_accession_number(uniprot_id):
    """Get the Accession number according to the UniProt ID."""
    url = f"https://rest.uniprot.org/uniprotkb/search?query=id:{uniprot_id}&fields=accession"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]['primaryAccession']  # Returns the first Accession number that matches
        else:
            return "No match found"
    else:
        return "API Error"

# Query Accession number for each UniProt ID
data['Entry_Number'] = data['UniProt_ID'].apply(fetch_accession_number)

# Save the updated CSV file
data.to_csv('C:/Users/Lenovo/Desktop/dissertation/indel/updated_file.csv', index=False)
