#!/usr/bin/python

import math
import sys
import numbers

try:
	a = float(sys.argv[1]) + 5
	print('wow you so fly. your new number is = {0} and you should feel happy.'.format(a))
except ValueError:
	raise ValueError('Invalid input: "{0}"; Please try again.'.format(sys.argv[1]))
