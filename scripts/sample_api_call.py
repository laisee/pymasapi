from pprint import pprint

import requests

url = 'https://eservices.mas.gov.sg/api/action/datastore/search.json?resource_id=9a51d255-fec1-4aca-9818-b7a47490243c'
response = requests.get(url)
pprint(response.json())
