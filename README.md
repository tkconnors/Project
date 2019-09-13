# Project
Sci-Coder-2019 FITS project

Contact Information for group members
Tae Pyo: tspyo, pyo@naoj.org
Tony Connors: tkconnors, tconnors@keck.hawaii.edu	
Alan Hatakeyama: inspgad, ahatakeyama@keck.hawaii.edu

Class Spectra_header_
File: Spectra_header.py_

Creation:
myFitsHead = Spectra_header("NameofFile")

Methods:
get_exptime()
get_obstime()
get_humidity()
get_gustspeed()
get_windspeed()
get_dec()

Notes:
Write your SDSSData module code as a function.  So that user calls a function in SDSSData
module. See calcAirMass.py and myTest.py

Importing
To import Spectra_header within SDSSData module code for example, calcAirMass.py use:
from Spectra_header import Spectra_header

To import for user software that calls a function within SDSSData module use the following.  See
myTest.py which uses allAirMass in calcAirMass.py contained in the SDSSData module.  See myTest.py
from SDSSData import calcAirMass

Add ~/Project to $PYTHONPATH.  I used:
export PYTHONPATH="/Users/inspectorgadget/SciCoder-2019-Keck/Data Files/spectra/Project"


Examples: see test.py in Project/SDSSData (tests Spectra_header object creation and methods )
		 see myTest.py uses SDSSData module by importing calcAirMass.
         see calcAirMass in ~/Project/SDSSData to see to use Spectra_header class.  Also shows
         how to calculate airmass for all files in the directory.

