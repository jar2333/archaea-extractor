from bs4 import BeautifulSoup
import requests
import re
import json

bac_dict = {}
soup = BeautifulSoup(open("Taxonomy_browser_Archaea.html"), 'html.parser')

initial = soup.find_all(type='square')

#the way it works, we only need a simple for loop. Neat!
for li in initial:
    bacterium = li.a
    bacterium_name = str(bacterium.strong.string)
    bacterium_link = "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/" + str(bacterium['href'])
    
    #taxonomy_id acquisition
    main_page = BeautifulSoup(requests.get(bacterium_link).content, 'html5lib')
    
    taxonomy_id = main_page.find(string=re.compile("txid"))
    taxonomy_id = taxonomy_id[taxonomy_id.index("txid")+4:len(taxonomy_id)-1]
    print(taxonomy_id)
    if taxonomy_id != None:
        bac_dict[taxonomy_id] = {"name" : bacterium_name, "link" : bacterium_link}

with open('archaea.txt', 'w') as outfile:
    json.dump(bac_dict, outfile)
    
