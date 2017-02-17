#!/usr/bin/python

#defining the filename
filename='aravg.ann.land_ocean.90S.90N.v4.0.1.201612.asc'
wxdata = {'year':[],'anomaly':[]}	#define dictionary

#open a file and read its contents
with open(filename, "r") as f: #read all the lines in the file
	alist = f.read().splitlines()

#looping over all the lines in the file
for line in alist: #iterate through lines
	wxdata['year'].append(int(line.split()[0]))
	wxdata['anomaly'].append(float(line.split()[1]))

DATA = zip(wxdata['year'],wxdata['anomaly'])
DATA = sorted(DATA, key=lambda x: x[1], reverse=True)

newfile = open('top10warmest.txt', 'w+')
print >> newfile, ("Ranking\tYear\tTemperature Anomaly (degrees C)\tTemperature Anomaly (degrees f)")

num = 0

for i in DATA[:10]:
	num += 1
	print >> newfile, "{0:1d}.\t{1:4d}\t{2:4f}\t\t\t{3:4f}".format(num, i[0], i[1], i[1]*9/5)

list (newfile)
