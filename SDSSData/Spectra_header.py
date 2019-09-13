#!/usr/bin/env python

import sys, math
from astropy.io import fits

class Spectra_header(object) :

	def __init__(self, fileName):
		self.windSpeed = None
		self.gustSpeed = None
		self.humidity = None
		self.expTime = None
		self.obsTime = None
		self.declination = None
		
		try:
			hdu_list = fits.open(fileName)
		except FileNotFoundError:
			print ("\n\n***** Spectra_Header: ERROR! Input file '" + str(fileName) + "' not found." + " Check directory.  *****")
		else:
			for hdu1 in hdu_list:
				#print(hdu1.header) # prints header
				#print(hdu_list.info())
				for key, value in hdu1.header.items():
					if key == "WINDS":
						#print("{0} = {1}".format(key,value))
						self.windSpeed = value
						#print("Spectra_header.windSpeed = %3.9f" % self.windSpeed)
					if key == "HUMIDITY" :
						self.humidity = value
						#print("Spectra_header.humidity = %2.9f" % self.humidity)
					if key == "GUSTS" :
						self.gustSpeed = value
						#print("Spectra_header.gustSpeed = %3.9f" % self.gustSpeed)
					if key == "SPCOADD" :
						self.obsTime = value
						#print ("Spectra_header.obsTime = %s" % self.obsTime)
					if key == "EXPTIME" :
						self.expTime = value
						#print ("Spectra_header.expTime = %d" % self.expTime)
					if key == "DECDEG" :
						self.declination = value
						#print ("Spectra_header.declination = %3.9f" % self.declination)
			
			#print ("\n\n\n")
		
			hdu_list.close()
		
	
	def get_exptime(self) :
		return self.expTime
		
	def get_obstime(self) :
		return self.obsTime
		
	def get_windspeed(self) :
		return self.windSpeed
		
	def get_humidity(self) :
		return self.humidity
		
	def get_gustspeed(self) :
		return self.gustSpeed
	
	def get_dec(self):
		return self.declination
		