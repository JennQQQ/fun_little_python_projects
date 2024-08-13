#########
#1. COPY the testcase table then paste it AS ONE LINE
#2. Each cell content CAN BE separated by spaces
#########
import numpy as np
import pandas as pd

col = {}
string = input('Table:')
table={}

text = string.split()

count = 0
for word in text:
    if '-' in word:
        break
    if '|' not in word:
        col[count]=word
    else:
        count+=1
count-=1

line_count = 0
ct = 1
line = 1
temp = ''

text = text[4*count+1:]

for i in range(len(text)-1):
    word=text[i]
    if word=="||":
        #temp=''
        ct=1
        line+=1
    elif word=="|":
        ct+=1
    elif 1<=ct<=count:
        if col[ct] not in table.keys():
            table[col[ct]]=[]
        if "|" not in text[i+1]:
            temp+=word
        if "|" in text[i+1]:
            temp+=' '+word
            table[col[ct]].append(temp)
            temp=''
        
query = pd.DataFrame(table)

print("The table has:", count, "columns")
print("-------------:", line, "rows")
print(query)
