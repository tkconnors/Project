#!/usr/bin/env python
import argparse
import sys, math, os
from astropy.io import fits
from Spectra_header import Spectra_header
# PYTHONPATH='/Users/tony/Desktop/Repositories/Project/'

# Argparse, still need to fix to take in a directory with multiple fit files
parser = argparse.ArgumentParser(description="This program reads FITS files and prints the exposure time for all cameras.",
								usage="name_of_script --filename spectrum.FITS")
parser.add_argument("-f", "--filename", help="FITS file to open")
args = parser.parse_args()

# location = "/Users/tony/Desktop/Repositories/Project/spectra/spec-4055-55359-0010.fits"

	# Create object
exposure_time=Spectra_header(args.filename) 
time=exposure_time.get_exptime()	# Minimum of exposure times for all cameras 

print(f'{args.filename} minimum exposure time for all cameras is {time} seconds.')
