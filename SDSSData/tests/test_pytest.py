#!/usr/bin/env python

import sys, math
from SDSSData import Spectra_header
from astropy.io import fits


def check_Spectra_header(fName):
	# Check that we can read a spectrum file.
	fitsHead = Spectra_header.Spectra_header(fName)
	#assert len(fitsHead.hdu_list) == 3, "Unexpected number of HDUs found in file."

	# Check humidity
	humidity = fitsHead.get_humidity()
	assert humidity is not None, "humidity = None"
	print ("fitsHead.humidity = %3.9f" % humidity)

	# Check windspeed
	windSpeed = fitsHead.get_windspeed()
	assert windSpeed is not None, "windSpeed = None"
	print ("fitsHead.windSpeed = %3.9f" % windSpeed)

	# Check gust speed
	gustSpeed = fitsHead.get_gustspeed()
	assert gustSpeed is not None, "gustSpeed = None"
	print ("fitsHead.gustSpeed = %3.9f" % gustSpeed)

	# Check observation
	obsTime = fitsHead.get_obstime()
	assert obstime is not None, "obstime = None"
	print ("fitsHead.obstime = %s" % fitsHead.get_obstime())

	# Check exposure time
	expTime = fitsHead.get_exptime()
	assert expTime is not None, "expTime = None"
	print ("fitsHead.exptime = %d" % expTime)

	# Check declination
	declination = fitsHead.get_dec()
	assert declination is not None, "declination = None"
	print ("fitsHead.declination = %3.9f" % declination)
	print("\n")

def test_goodSpectra():
	# Check a good .fits file.
	check_Spectra_header("../../spectra/spec-4055-55359-0001.fits")

def test_noWeather():
	# Check a .fits file that's missing weather data.
	check_Spectra_header("../../spectra/spec-10000-57346-0002.fits")
	
def test_badFile():
	# Check a non-existant fits file.
	check_Spectra_header("junk.fits")
	
test_goodSpectra()
#test_noWeather()
#test_badFile()

