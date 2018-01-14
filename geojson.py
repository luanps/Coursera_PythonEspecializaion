''' extract json data from web'''

import urllib #.request, urllib.parse, urllib.error
import json
import pdb
# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location: ')

url = serviceurl + urllib.urlencode(
    {'address': address})

uh = urllib.urlopen(url)
data = uh.read().decode()
try:
    js = json.loads(data)
except:
    js = None

pl_id = str(js['results'][0]['place_id'])
print('Place id %s'% pl_id)
