from  urllib2 import urlopen
import json
serviceurl = 'http://py4e-data.dr-chuck.net/comments_59032.json'
data = urlopen(serviceurl).read()
info = json.loads(data)
count = 0
for i in info['comments']:
    count += int(i['count'])
print(count)

