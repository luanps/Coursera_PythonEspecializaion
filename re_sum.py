''' 
using re (regular expression) to 
extract data from file
'''

import sys
import re
num=0
s_num=0
with open(sys.argv[1],'r') as f:
    for ln in f:
        tmp =  re.findall('[0-9]+',ln)
        if tmp:
            num = sum([int(x) for x in tmp])
            s_num += num
print(s_num)
       
