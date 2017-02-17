#!/usr/bin/python

#defining the filename
filename = 'CMI.csv'
cdict = {'station':[],'valid':[],'tmpf':[],'presentwx':[]}

#open file, read its contents
with open(filename, "r") as f:
        clist = f.read().splitlines()

#separate columns into the dictionary keys
for line in clist:
        cdict['station'].append(line.split(',')[0])
        cdict['valid'].append(line.split(',')[1])
        cdict['presentwx'].append(line.split(',')[-1])

#initialize SN counter
SN=0

#begin incrementing SN counter by searching each string in list
for i in cdict['presentwx']:
	if (' SN ' in i) or ('+SN' in i) or ('-SN' in i) or ('SN ' in i):
		print (i)
		SN+=1

#print(len(cdict['presentwx']))
print("Total reports of snow: {0}".format(SN))

