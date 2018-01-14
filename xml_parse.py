'''
Extracting xml data from web
'''

from  urllib2 import urlopen
import xml.etree.ElementTree as ET
serviceurl = 'http://py4e-data.dr-chuck.net/comments_59031.xml'
data = urlopen(serviceurl).read()
tree = ET.fromstring(data)
counts = (tree.findall('.//count'))
count = 0
for i in counts:
    count += int(i.text)
print(count)
