#########
#1. COPY the testcase table then paste it AS ONE LINE
#2. Each cell content can not be separated by any space
#########

import numpy as np
import pandas as pd

col = {}
string = input('Table:')
table={}

count = 0
for word in string.split():
    if '-' in word:
        break
    if '|' not in word:
        col[count]=word
    else:
        count+=1
count-=1

line_count = 0
ct = 0

for word in string.split():
    if word=="||":
        ct=1
    elif word=="|":
        ct+=1
    elif word not in col.values() and 1<=ct<=count:
        if "--" not in word:
            if col[ct] not in table.keys():
                table[col[ct]]=[]
            table[col[ct]].append(word)
        
query = pd.DataFrame(table)

print(query)
