'''
Retrieving webpages from web recursively
using BeatifulSoup
'''

from  urllib2 import urlopen
from bs4 import BeautifulSoup
import pdb
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count =input('Enter count - ')
pos =input('Enter position - ')
for i in range(0,count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    print('Retrieving: ',url)
    for j,tag in enumerate(tags):
        if j==pos-1:
            url = tag.attrs['href']
            name = str(tag.text)
print(name)
