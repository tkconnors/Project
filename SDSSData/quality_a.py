#! /usr/bin/env python

import sys
import os
import argparse
from Spectra_header import Spectra_header

from astropy.io import fits

default_data_folder = "/Users/tspyo/SciCoder-2019-Keck/Data Files/spectra/"

parser = argparse.ArgumentParser(description="This program shows HDU information for FITS file",
                         usage="name_of_script --folder_path <your_data_path>",
                         epilog="good luck")
                         
parser.add_argument("-f", "--folder_path",
                    help="the FITS files to read")
                    
args = parser.parse_args()


if (len(sys.argv) < 2):
	data_folder = default_data_folder
else:
	data_folder = args.folder_path
	
fits_filelist = list()

print(data_folder)

print("#---fits file---EXPTIME(s)---WINDS(GUSTS)---HUMIDITY(%)#")
for filename in os.listdir(data_folder) :
	if filename.endswith(".fits"):
		fits_file = data_folder + filename
		#print(f"Fits file = {filename}")
		fits_header = Spectra_header(fits_file)
		f_exptime = fits_header.get_exptime()
		f_windspeed = fits_header.get_windspeed()
		f_gustspeed = fits_header.get_gustspeed()
		f_humidity = fits_header.get_humidity()
		print(f"{filename}: {f_exptime} s, {f_windspeed}({f_gustspeed}), {f_humidity}")
		if (f_windspeed == None):
			print ("!!!Warning !!!! No windspeed information")
			print("\n")
		elif (float(f_windspeed) > 10.):
			print(f"!!!! Wind speed is so fast = {f_windspeed} !!!!")
			print("\n")
		if(f_humidity == None):
			print("!!!Warning !!!! No Humidity information")
			print("\n")
		elif (float(f_humidity) > 70.):
			print(f"!!!! High Humidity condition = {f_humidity}% !!!!")
			print("\n")
        
        

	

	


