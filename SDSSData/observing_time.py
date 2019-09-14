#!/usr/bin/env python
import argparse
import sys, math, os
from astropy.io import fits
from Spectra_header import Spectra_header
# PYTHONPATH='/Users/tony/Desktop/Repositories/Project/'

# Argparse, still need to fix to take in a directory with multiple fit files
parser = argparse.ArgumentParser(description="This program reads FITS files and prints the observation date for all cameras.",
								usage="name_of_script --filename spectrum.FITS")
parser.add_argument("-f", "--filename", help="FITS file to open")
args = parser.parse_args()

# location = "/Users/tony/Desktop/Repositories/Project/spectra/spec-4055-55359-0010.fits"

	# Create object
observation_time=Spectra_header(args.filename) 
date=observation_time.get_obstime()	# SPCOADD finished (Not really observation date/time)

print(f'{args.filename} data was observed on {date}.')
