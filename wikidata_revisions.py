import numpy as np
import pandas as pd

import urllib.request
from bs4 import BeautifulSoup
import json

from tqdm import tqdm

DATA = pd.read_csv("phd_query - Arkusz1.csv") 

wiki_ids = list(DATA["ID"])

def get_response(wiki_id : str):

  '''

  Function for getting responses from wikidata api. 

  Function accepts single wikidata id (Q) as a parameter.

  In each query, need to define query parameters such as query id (Q) (stored in function parameter), properties
  of query (list of properties is available here: ) and sorting type. Each parameter should be separated by | (pipe) 
  (without any spaces between values and separator) and placed in single string.

  Function returns data in (json) dictionary format. 


  '''

  title = wiki_id
  props = "ids|timestamp|flags|comment|user"
  sort = "newer"
  URL = f"""https://www.wikidata.org/w/api.php?action=query&format=json&prop=revisions&titles={title}&rvprop={props}&rvdir={sort}"""
  
  open_url = urllib.request.urlopen(URL)
  
  if(open_url.getcode() == 200):
      data = oper_url.read()
      json_data = json.loads(data)
  else:
      print("Error receiving data", open_url.getcode())
  return json_data

def get_wikidata_revisions(list_of_q : list):

  '''

  Function for querying wikidata api with list of wikidata ids (Q)

  Function accepts list of Qs in list format

  Function uses get_response function as a base.

  Function returns both data in dict format and file in json format, where key is
  wikidata id (Q) and value is response from wikidata api

  '''

  result = {}


  for wiki_id in tqdm(list_of_q):
    result[wiki_id] = get_response(wiki_id)

  with open("data.json", "w") as outfile:
    json.dump(result, outfile)

  return result



result = get_wikidata_revisions(wiki_ids)
