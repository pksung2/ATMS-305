#!/usr/bin/python

#defining the filename
filename = 'CMI.csv'
cdict = {'station':[],'valid':[],'tmpf':[],'presentwx':[]}

#open file, read its contents
with open(filename, "r") as f:
        clist = f.read().splitlines()[1:]

#separate columns into the dictionary keys
for line in clist:
        cdict['station'].append(line.split(',')[0])
        cdict['valid'].append(line.split(',')[1])
        cdict['tmpf'].append(line.split(',')[2])
        cdict['presentwx'].append(line.split(',')[-1])

#initialize SN counter
SN=0

#begin incrementing SN counter by searching each string in list
for i in cdict['presentwx']:
	if 'SN' in i:
#		print (i)
		SN+=1

#make highest temperature and date available
temperature = sorted(zip(cdict['tmpf'], cdict['valid']))

#initialize total temperature counter
total=0
temptotal=0

#find highest temperature recorded
for i in temperature:
        try:
                float(i[0])
                temp = i
		total += 1
		temptotal+=float(i[0])
        except ValueError:
                pass

#print(len(cdict['presentwx']))
print("Total reports of snow: {0}".format(SN))
print("Fraction of reports with snow: {0}/{1}".format(SN, len(cdict['presentwx'])))
print("Highest temperature: {0}F at {1}".format(temp[0], temp[1]))
print("Mean temperature: {0:5.2f}F".format(temptotal/total))
