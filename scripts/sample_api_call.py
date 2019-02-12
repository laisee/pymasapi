import requests
from pprint import pprint
response = requests.get('https://api.spotify.com/v1/search?type=artist&q=snoop').json()
pprint(r.json())
