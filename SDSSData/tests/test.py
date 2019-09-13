#!/usr/bin/env python

import sys, math
from SDSSData import Spectra_header
from astropy.io import fits

fitsHeader = Spectra_header.Spectra_header("../../spectra/spec-10000-57346-0002.fits")
print ("fitsHeader.humidity = %3.9f" % fitsHeader.get_humidity())
print ("fitsHeader.windspeed = %3.9f" % fitsHeader.get_windspeed())
print ("fitsHeader.gustspeed = %3.9f" % fitsHeader.get_gustspeed())
print ("fitsHeader.obstime = %s" % fitsHeader.get_obstime())
print ("fitsHeader.exptime = %d" % fitsHeader.get_exptime())
print ("fitsHeader.declination = %3.9f" % fitsHeader.get_dec())
print("\n\n")


# Example of fits file without "weather" information.
fitsNoWeather = Spectra_header.Spectra_header("../../spectra/spec-4055-55359-0001.fits")
humidity = fitsNoWeather.get_humidity()
if humidity is not None:
	print ("fitsNoWeather.humidity = %3.9f" % humidity)
else:
	print ("fitsNoWeather.humidity = None")
windSpeed = fitsNoWeather.get_windspeed()
if windSpeed is not None:
	print ("fitsNoWeather.windSpeed = %3.9f" % windSpeed)
else:
	print ("fitsNoWeather.windSpeed = None")
gustSpeed = fitsNoWeather.get_gustspeed()
if gustSpeed is not None:
	print ("fitsNoWeather.gustSpeed = %3.9f" % gustSpeed)
else:
	print ("fitsNoWeather.gustSpeed = None")
print ("fitsNoWeather.obstime = %s" % fitsNoWeather.get_obstime())
print ("fitsNoWeather.exptime = %d" % fitsNoWeather.get_exptime())
print ("fitsNoWeather.declination = %3.9f" % fitsNoWeather.get_dec())
print("\n")

# Example of missing fits file.
badfitsHeader = Spectra_header.Spectra_header("junk.fits")
print ("badfitsHeader.humidity = %s" % badfitsHeader.get_humidity())
print ("badfitsHeader.windspeed = %s" % badfitsHeader.get_windspeed())
print ("badfitsHeader.gustspeed = %s" % badfitsHeader.get_gustspeed())
print ("badfitsHeader.obstime = %s" % badfitsHeader.get_obstime())
print ("badfitsHeader.exptime = %s" % badfitsHeader.get_exptime())
print ("badfitsHeader.declination = %s" % badfitsHeader.get_dec())
