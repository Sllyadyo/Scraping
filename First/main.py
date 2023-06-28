from Parsefirst import site_parsing
from Parsesecond import OneUrlScrap

import csv

urls = site_parsing()

with open("./notebooks_data.csv", "w", encoding='utf-8', newline="") as file:
    print('data cleared')

with open("./notebooks_data.csv", "a", encoding='utf-8', newline="") as file:
    print('data scraping......')
    
    # list of dictionaries containing notebooks
    notebooks = []
    
    for url in urls:
        notebooks.append(OneUrlScrap(url))

    writer = csv.DictWriter(file, fieldnames=notebooks[0].keys())
    
    # Write the CSV file header
    writer.writeheader()
    
     # Write data from the dictionary list
    for row in notebooks:
        writer.writerow(row)
     
    print('Successfully saved in notebooks_data.csv')

      

    