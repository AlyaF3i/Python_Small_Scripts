import csv
import numpy as np
Ola=open('data.csv')
f=list(csv.reader(Ola))
map={
    'Europe':{},
    'South-East Asia':{},
    'Americas':{},
    'Africa':{},
    'Eastern Mediterranean':{},
    'Western Pacific':{},
    'Other':{}
}
for a in range(1,len(f)):
    if f[a][1]=='':
        continue
    map[f[a][1]][f[a][0]]=int(f[a][2])
newMap={
    'Europe':0,
    'South-East Asia':0,
    'Americas':0,
    'Africa':0,
    'Eastern Mediterranean':0,
    'Western Pacific':0,
    'Other':0
}
for a in map:
    sum=0
    for c in map[a]:
        sum+=map[a][c]
    newMap[a]=sum
newMap=dict(sorted(newMap.items(), key=lambda item: item[1]))
print(newMap)

