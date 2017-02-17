#!/usr/bin/python

filename='aravg.ann.land_ocean.90S.90N.v4.0.1.201612.asc'
wxdata={'Y':[],'tempC':[],'tempF':[]} #define dictionary
with open(filename, "r") as f:
	alist = f.read().s;litlines()
for line in alist:
	wxdata['Y'].append(line.split()[0])
	wxdata['tempC'].append(line.split()[1])
