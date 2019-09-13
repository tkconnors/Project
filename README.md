# Project
Sci-Coder-2019 FITS project

Contact Information for group members
Tae Pyo: tspyo, pyo@naoj.org
Tony Connors: tkconnors, tconnors@keck.hawaii.edu	
Alan Hatakeyama: inspgad, ahatakeyama@keck.hawaii.edu

Class Spectra_header_
File: Spectra_header.py_

Importing Spectra_header use the following:
from Spectra_header import Spectra_header

Creation:
myFitsHead = Spectra_header("NameofFile")

Methods:
get_exptime()
get_obstime()
get_humidity()
get_gustspeed()
get_windspeed()
get_dec()

Example: see test.py in Project/SDSSData
         see calcAirMass in Project/SDSSData to see how to calculate airmass for all files in the directory.

