# Indexes a document in Solr+mtas.
# Input format is a JSON file with the following format:
#
#   {"title": "Totally Terrible Title",
#    "author": "An Awesome Anonymous Author",
#    "year": 1999,
#    "text": "<FoLiA xmlns:xlink=\"http://www.w3.org/1999/xlink\" ..."}
#
# All four fields must be filled in. The text must be a FoLiA document
# (escaped to fit in JSON, of course).
#
# Note: this is a wrapper around a single POST request.

import json
import sys

import requests

base_url, username, core = sys.argv[1:4]

payload = [json.load(os.stdin)]

# Username + _ + core becomes the 'actual' core name as Solr sees it.
r = requests.post('%s/solr/%s_%s/update?wt=json&commit=true'
                  % (base_url, username, core),
                  json=payload)
print(r.content)
