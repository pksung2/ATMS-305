#!/usr/bin/python

filename='aravg.ann.land_ocean.90S.90N.v4.0.1.201612.asc'
wxdata = {'year':[],'temperature':[]}	#define dictionary

with open(filename, "r") as f: #read all the lines in the file
	alist = f.read().splitlines()

for line in alist: #iterate through lines
	wxdata['year'].append(int(line.split()[0]))
	wxdata['temperature'].append(float(line.split()[1]))

print(len(wxdata['year']))
# print(year)
