#!/usr/bin/python

import math
import sys
import numbers

a = len(sys.argv)

if a == 2:
	try:
		T = float(sys.argv[1])
                sat = 6.1094 * math.exp(17.625*T/(T+243.04))
                print ('\nThe saturation vapor pressure temperature is:\n{0}\n'.format(sat))
	except:
		print 'Please input a valid thing.'
elif a > 2:
	print "Too many inputs."

else:
	print "Please input a water temperature."
