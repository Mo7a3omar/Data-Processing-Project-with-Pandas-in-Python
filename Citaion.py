import pandas as pd 
import numpy as np
import csv
from collections import Counter

#writer = csv.writer(open("out.csv", "wb"), quoting=csv.QUOTE_NONE)
#reader = csv.reader(open("in.csv", "rb"), skipinitialspace=True)

file = pd.read_csv('Nodes.csv', quoting = csv.QUOTE_NONE, on_bad_lines = 'skip')
nodes = pd.DataFrame()
nodes['id'] = file.iloc[:,0]
nodes['name'] = file.iloc[:,1]
#o(n)
#print(nodes)
#print(len(nodes))

file2 = pd.read_csv('Edges.csv', quoting=csv.QUOTE_NONE, on_bad_lines='skip')
edges = pd.DataFrame()
edges['id'] = file2.iloc[:,0]
edges['Cid'] = file2.iloc[:,1]
#o(n)
#print(edges)
#print(len(edges))

enjoin = nodes.join(edges.set_index('id'), on='id', how='left', lsuffix='_left', rsuffix='_right')
#enjoin = edges.join(nodes.set_index('id'), on='id', how='left', lsuffix='_left', rsuffix='_right')

print(enjoin)
x = dict()
for i in range(len(enjoin)):
  if enjoin.iloc[i,1] in x:
    x[enjoin.iloc[i,1]].append(enjoin.iloc[i,0]) 
  else:
    x[enjoin.iloc[i,1]] = [enjoin.iloc[i,0]]

no_of_papers = []
for i in x:
  no_of_papers.append(len(x[i]))
#print (no_of_papers)
print(len(x))


#most_common= dict()
#for i in x :
#  most_common["id"] = enjoin.iloc[:,0]
#  most_common["name"] = enjoin.iloc[:,1]
#  most_common["cid"] = enjoin.iloc[:,2]
#most_common = sorted(most_common(by=['cid']))
#most_common = most_common.sort_values(by=['cid'], ascending = False)
#print(most_common)
#high = max(most_common.values())
#high_index = most_common.    
#highest = list(enjoin)[high_index]
#print(high)
#print(highest)
  

Final = pd.DataFrame()
Final['id'] = x
Final['cid'] = no_of_papers
Final = Final.sort_values(by=['cid'], ascending = False)
Final.to_csv('Final.csv')
print(Final)
highest = max(no_of_papers)
high_index = no_of_papers.index(highest)
Most_used= list(x)[high_index]
print(Most_used)
print(highest)

    
