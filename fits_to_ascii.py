#!/usr/bin/python

from astropy.io import ascii
from astropy.table import Table
import numpy as np
import pyfits
import argparse

parser = argparse.ArgumentParser(description='convert fits to ascii, the increment has to be constant, add input fits file')
parser.add_argument('input', help='Input file')
args = parser.parse_args()

hdulist = pyfits.open(args.input)
header = hdulist[0].header #read header
flux = hdulist[0].data #flux data in the primary
flux = np.array(flux, dtype=np.float64)

start_wave = header['CRVAL1'] #initial wavelenght
step = header['CDELT1'] #increment per pixel

new_wave = []
for i in range(0,len(flux)):
	 start_wave = start_wave + step*i
	 new_wave.append(start_wave)

data = Table([new_wave, flux], names=(str(header['CRVAL1']), str(step)))
ascii.write(data, args.input[:-5]+".dat", delimiter='\t')  #new file created
print '----------------------------------'
print 'fits to ascii: DONE'
