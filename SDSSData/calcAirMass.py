#!/usr/bin/env python

import sys, math, os
from Spectra_header import Spectra_header
from astropy.io import fits

location = "/Users/inspectorgadget/SciCoder-2019-Keck/Data Files/spectra/Project/spectra/"

for file in os.listdir(location) :

	if file.endswith(".fits"):
		file = location + file
		print("file = %s" % file)
		dataHead = Spectra_header(file)
		declination = dataHead.get_dec()
		if declination is not None:
			rad = (declination/180) * math.pi
			airMass = 1.0 / math.sin(declination * math.pi/180)
			print ("Air mass for declination %3.9f deg. = %3.9f\n" % (declination, airMass))
		else:
			print ("No declination information: cannot calculate air mass for %s" % file)
