#!/usr/bin/python

import math
import sys
import numbers

a = len(sys.argv)

if a == 2:

		T = float(sys.argv[1])
                sat = 6.1094 * math.exp(17.625*T/(T+243.04))
                print 'The saturation vapor pressure temperature is',sat

elif a > 2:
	print "Too many values."

else:
	print "Please input a water temperature."
